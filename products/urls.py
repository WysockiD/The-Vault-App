from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='all-products'), # our-domain.com/products
  path('<slug:product_slug>/success', views.confirm_registration, name='confirm-registration'),
  path('<slug:product_slug>', views.product_details, name='product-detail'), # our-domain.com/products/<dynamic-path-segment>
]