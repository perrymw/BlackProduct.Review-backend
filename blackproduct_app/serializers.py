from rest_framework.serializers import HyperlinkedModelSerializer
from blackproduct_app import models
# Serializers using the current models as of 08/26


class BusinessAddressSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.BusinessAddress
        fields = [
            'id',
            'address',
            'zip_code',
            'city',
            'country'
        ]


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


class BPRUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.BPRUser
        fields = [
            'id',
            'email',
            'is_staff',
            'is_active',
            'joined'
        ]


class ReviewsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Reviews
        fields = [
            'id',
            'content',
            'reviewer',
            'date_posted'
        ]


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'id',
            'like_or_dislike',
            'owned_by',
            'product_link',
            'tags',
            'posted_date',
            'photo',
            'traffic',
            'review'
        ]


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Comment
        fields = [
            'id',
            'content',
            'commenter'
        ]
