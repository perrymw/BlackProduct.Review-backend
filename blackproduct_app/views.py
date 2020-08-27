# from django.shortcuts import render
from rest_framework import viewsets
from blackproduct_app import models, serializers


# Create your views here.


class BusinessAddressViewSet(viewsets.ModelViewSet):
    queryset = models.BusinessAddress.all()
    serializer_class = serializers.BusinessAddressSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = models.Business.all()
    serializer_class = serializers.BusinessSerializer


class BPRUserViewSet(viewsets.ModelViewSet):
    queryset = models.BPRUser.all()
    serializer_class = serializers.BPRUserSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.all()
    serializer_class = serializers.ReviewsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.all()
    serializer_class = serializers.ProductSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.all()
    serializer_class = serializers.CommentSerializer
