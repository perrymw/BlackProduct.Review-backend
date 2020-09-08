# from django.shortcuts import render
from rest_framework.viewsets import *
from django.http import JsonResponse
from blackproduct_app import models, serializers


# Create your views here.


class BusinessAddressViewSet(ModelViewSet):
    queryset = models.BusinessAddress.objects.all()
    serializer_class = serializers.BusinessAddressSerializer


class BusinessViewSet(ModelViewSet):
    serializer_class = serializers.BusinessSerializer
    # Help acquired from Joe Kaufeld
    basename = 'business'

    def get_queryset(self):
        queryset = models.Business.objects.all().order_by('-name')
        method = self.request.query_params.get('name')
        return queryset
    lookup_field = 'name'

class BPRUserViewSet(ModelViewSet):
    queryset = models.BPRUser.objects.all()
    serializer_class = serializers.BPRUserSerializer


class ReviewsViewSet(ModelViewSet):
    queryset = models.Reviews.objects.all().order_by('-date_posted')
    serializer_class = serializers.ReviewsSerializer


class ProductViewSet(ModelViewSet):
    basename = 'products'
    queryset = models.Product.objects.all().order_by('-product_name')
    serializer_class = serializers.ProductSerializer
    lookup_field = 'product_name'


    def get_queryset(self):
        queryset = models.Product.objects.all().order_by('-product_name')
        method = self.request.query_params.get('product_name')
        return queryset



class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
