# from django.shortcuts import render
from rest_framework import viewsets
from blackproduct_app import models, serializers


# Create your views here.


class BusinessAddressViewSet(viewsets.ModelViewSet):
    queryset = models.BusinessAddress.objects.all()
    serializer_class = serializers.BusinessAddressSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer


class BPRUserViewSet(viewsets.ModelViewSet):
    queryset = models.BPRUser.objects.all()
    serializer_class = serializers.BPRUserSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
