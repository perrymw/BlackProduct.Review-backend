"""BlackProduct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from blackproduct_app.views import *

router = routers.DefaultRouter()
router.register(r'business_address',BusinessAddressViewSet )
router.register(r'business',BusinessViewSet, basename='name')
router.register(r'users',BPRUserViewSet )
router.register(r'reviews',ReviewsViewSet )
router.register(r'products', ProductViewSet , basename='product_name')
router.register(r'comments',CommentViewSet )
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)