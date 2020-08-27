from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


class BusinessAddress(models.Model):
    address = models.CharField(max_length=1000, null=False)
    zip_code = models.CharField(max_length=15, null=False)
    city = models.CharField(max_length=1000, null=False)
    #  https://github.com/SmileyChris/django-countries
    country = CountryField()


class Business(models.Model):
    name = models.TextField()
    owner = models.TextField()
    website = models.URLField(max_length=200, null=False)
    email = models.EmailField(max_length=254, null=False)
    address = models.OneToOneField(BusinessAddress, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class BPRUser(AbstractUser):
    email = models.EmailField(max_length=254, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


class Reviews(models.Model):
    # TODO Rating system for comment
    content = models.TextField(null=False)
    reviewer = models.ForeignKey(BPRUser, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    like_or_dislike = models.BooleanField(default=True)
    owned_by = models.ForeignKey(Business, on_delete=models.CASCADE)
    # TODO: make field choices for choicefield of types of products
    product_link = models.URLField(max_length=2000, default=None)
    # https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    tags = TaggableManager()
    posted_date = models.DateTimeField(default=timezone.now)
    photo = models.FileField(upload_to='media', max_length=1001)
    traffic = models.IntegerField()
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(null=False)
    commenter = models.ForeignKey(BPRUser, on_delete=models.CASCADE)
