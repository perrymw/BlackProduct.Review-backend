from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from localflavor.us.us_states import STATE_CHOICES


class BusinessAddress(models.Model):
    address = models.CharField(max_length=1000, null=False)
    zip_code = models.CharField(max_length=15, null=False)
    city = models.CharField(max_length=1000, null=False)
    state = models.CharField(choices=STATE_CHOICES,max_length=2)
    #  https://github.com/SmileyChris/django-countries
    country = CountryField()

    def __str__(self):
        return self.address


class Business(models.Model):
    name = models.TextField()
    owner = models.TextField()
    website = models.URLField(max_length=200,blank=True)
    email = models.EmailField(max_length=254, blank=False)
    address = models.OneToOneField(BusinessAddress, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class BPRUser(AbstractUser):
    email = models.EmailField(max_length=254, null=False)
    is_review_staff = models.BooleanField(default=False)
    is_bor_customer = models.BooleanFiels(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    display_name = models.CharField(max_length=100)
    saved_products = models.ManyToManyField('Product', related_name='favorites')
    saved_businesses = models.ManyToManyField('Business', related_name='favoritebusinesses+', symmetrical=False)


class Reviews(models.Model):
    content = models.TextField(null=False)
    reviewer = models.ForeignKey(BPRUser, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    product_type_choices = [
        ('HCSC', 'Hair Care/Skincare'),
        ('HHS', 'Household Staples'),
        ('F&D', 'Food & Drink'),
    ]
    product_name = models.TextField()
    owner = models.ForeignKey(Business, on_delete=models.CASCADE)
    product_choice = models.CharField(choices=product_type_choices, max_length=4, default="HCSC")
    product_link = models.URLField(max_length=2000, default=None)
    # https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    tags = TaggableManager(blank=True)
    posted_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='images/', max_length=1001)
    traffic = models.IntegerField(default=0)
    ratings = models.ManyToManyField(BPRUser, through="Rating", )
    review = models.ForeignKey(Reviews, related_name='review',on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.product_name
    
    def get_tags_display(self):
        return self.tags.values_list('tags', flat=True)

    @property
    def average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating.rating_sys
        return total/len(self.ratings)

    @property
    def owner_name(self):
        return self.owner.name



class Comment(models.Model):
    content = models.TextField(null=False)
    commenter = models.ForeignKey(BPRUser, on_delete=models.CASCADE)


class Rating(models.Model):
    rating_system_choices = [(num,str(num)) for num in range(1,6)]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rater = models.ForeignKey(BPRUser, on_delete=models.CASCADE)
    rating_sys = models.IntegerField(choices=rating_system_choices, default=1)

    class meta:
        unique_together = ('product','rater')
