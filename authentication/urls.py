
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset

router = DefaultRouter()
router.register('user', UserViewset, basename='user')

urlpatterns = [
    path('', include(router.urls))
]