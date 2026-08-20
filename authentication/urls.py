from django.urls import path
from authentication.views import RegisterAPI, MyProfileAPI

urlpatterns = [
    path('register/',RegisterAPI.as_view(), name='register'),
    path('my-profile/', MyProfileAPI.as_view(), name='my_profile'),
]
