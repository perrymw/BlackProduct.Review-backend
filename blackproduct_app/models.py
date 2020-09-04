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
    address = models.OneToOneField(BusinessAddress, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class BPRUser(AbstractUser):
    email = models.EmailField(max_length=254, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    display_name = models.CharField(max_length=100)


class Reviews(models.Model):
    # TODO Rating system for review
    content = models.TextField(null=False)
    reviewer = models.ForeignKey(BPRUser, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    product_name = models.TextField()
    like_or_dislike = models.BooleanField(default=True)
    owner = models.ForeignKey(Business, on_delete=models.CASCADE)
    # TODO: make field choices for choicefield of types of products
    product_link = models.URLField(max_length=2000, default=None)
    # https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    tags = TaggableManager()
    posted_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='images/', max_length=1001)
    traffic = models.IntegerField(default=0)
    # TODO Rating system for review
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.OneToOneField(BPRUser, on_delete=models.CASCADE, unique=True, blank=True, null=True)

# 

class Comment(models.Model):
    content = models.TextField(null=False)
    commenter = models.ForeignKey(BPRUser, on_delete=models.CASCADE)
