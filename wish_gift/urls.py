from django.urls import path
from . import views

urlpatterns = [
    path('', views.gift_list, name='gift_list'),
    path('lists/<int:pk>', views.gift_detail, name='gift_detail'),
    path('lists/<int:pk>/delete', views.gift_delete, name='gift_delete'),
    path('lists/new', views.gift_create, name='gift_create'),
]
