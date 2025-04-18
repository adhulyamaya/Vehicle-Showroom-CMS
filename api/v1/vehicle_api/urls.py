from django.urls import path
from . import views


app_name = 'vehicle_api'


urlpatterns = [
    
    path('categories/',views.get_category_list,name='category_list'),
    path('categories/create/',views.create_category,name='category-create'),
    path('categories/<int:id>/update/',views.update_category,name='category-update'),
    path('categories/<int:id>/delete/',views.delete_category,name='category-delete'),

    path('vehicles/',views.get_vehicle_list,name='vehicle_list'),
    path('vehicles/<int:id>/',views.get_vehicle_by_id,name='vehicle-detail'),
    path('vehicles/create/',views.create_vehicle,name='vehicle-create'),
    path('vehicles/<int:id>/update/',views.update_vehicle,name='vehicle-update'),
    path('vehicles/<int:id>/delete/',views.delete_vehicle,name='vehicle-delete'),

    path('variants/',views.get_variant_list,name='variant_list'),
    path('variants/create/',views.create_variant,name='variant-create'),
    path('variants/<int:id>/update/',views.update_variant,name='variant-update'),
    path('variants/<int:id>/delete/',views.delete_variant,name='variant-delete'),

    path('vehicle-prices/', views.get_vehicle_price_list, name='vehicle-price-list'),
    path('vehicle-prices/create/', views.create_vehicle_price, name='vehicle-price-create'),
    path('vehicle-prices/<int:id>/update/', views.update_vehicle_price, name='vehicle-price-update'),
    path('vehicle-prices/<int:id>/delete/', views.delete_vehicle_price, name='vehicle-price-delete'),
]