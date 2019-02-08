
from django.conf.urls import url , include
from django.contrib import admin 
from .views import Cityviewset ,Tourviewset
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

#router.register(r'destination' , views.Destinationviewset)


router = DefaultRouter()
router.register(r'tour' , Tourviewset)
router.register(r'city' , Cityviewset)

urlpatterns = [
    url(r'^' , include(router.urls)),
    url(r'^docs/' , include_docs_urls(title='tour API')),
]
