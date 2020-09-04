from rest_framework.serializers import HyperlinkedModelSerializer
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
    address = BusinessAddressSerializer()


class BPRUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.BPRUser
        fields = [
            'id',
            'username',
            'password',
            'email',
            'is_staff',
            'is_active',
            'date_joined'
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
    reviewer = BPRUserSerializer()


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'id',
            'owner',
            'product_link',
            'tags',
            'posted_date',
            'rating',
            'review',
            'photo',
            'traffic',
            'review',
            'like_or_dislike',
        ]
    review = ReviewsSerializer()
    rating = BPRUserSerializer()


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Comment
        fields = [
            'id',
            'content',
            'commenter'
        ]
    commenter = BPRUserSerializer()