from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexPageView.as_view(), name='index'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('search/', search, name='search'),
]