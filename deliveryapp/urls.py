
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make_order/', views.make_order, name='make_order'),
    path('order_list/', views.order_list, name='order_list'),
    path('assign_deliverer/<int:order_id>/', views.assign_deliverer, name='assign_deliverer'),
]
