# from django.shortcuts import render
from rest_framework import viewsets

from blackproduct_app import models, serializers


# Create your views here.


class BusinessAddressViewSet(viewsets.ModelViewSet):
    queryset = models.BusinessAddress.objects.all()
    serializer_class = serializers.BusinessAddressSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BusinessSerializer
    # Help acquired from Joe Kaufeld
    basename = 'business'

    def get_queryset(self):
        queryset = models.Business.objects.all().order_by('-name')
        method = self.request.query_params.get('name')
        return queryset
    lookup_field = 'name'

class BPRUserViewSet(viewsets.ModelViewSet):
    queryset = models.BPRUser.objects.all()
    serializer_class = serializers.BPRUserSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.all().order_by('-date_posted')
    serializer_class = serializers.ReviewsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Business.objects.all()
        method = self.request.query_params.get('product_name')
        return queryset
    lookup_field = 'product_name'


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
