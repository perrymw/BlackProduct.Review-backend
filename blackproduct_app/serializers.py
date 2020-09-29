from rest_framework.serializers import *
from blackproduct_app import models
# Serializers using the current models as of 08/26


class BusinessAddressSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.BusinessAddress
        fields = '__all__'

class BusinessSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Business
        fields = [
            'id',
            'name',
            'owner',
            'website',
            'email',
            'address',
            'date'
        ]


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = [
            'id',
            'content',
            'reviewer',
            'date_posted'
        ]



class TagListField(ListField):
    child = CharField()

    def to_representation(self, data):
        return ' '.join(data.values_list('name', flat=True))

class ProductSerializer(ModelSerializer):

    tags = TagListField()

    class Meta:
        model = models.Product
        fields = [
            'id',
            'product_name',
            'owner',
            'product_link',
            'tags',
            'posted_date',
            'rating',
            'review',
            'photo',
            'traffic',
            'review',
        ]



class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = [
            'id',
            'content',
            'commenter'
        ]
