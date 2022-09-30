from django.urls import path
from sales import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.SalesList.as_view()),
    path('wisher/<int:pk>', views.Wisher.as_view()),
    path('products/', views.ProdcuctList.as_view()),
    path('product/<int:pk>/', views.productcrud.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)