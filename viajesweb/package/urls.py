from django.urls import path
from .views import PackageListView, PackageDetailView

urlpatterns = [
	path('packages/', PackageListView.as_view(), name='packages'),
	path('buy/<int:pk>/', PackageDetailView.as_view(), name='buy'),
]