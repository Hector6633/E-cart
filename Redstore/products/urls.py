from django.urls import path,include
from django.conf.urls.static import static
from .  import views


urlpatterns = [
   path('',views.index,name='index'),
   path('products_list',views.products_list,name='products_list'),
   path('products_details/<pk>',views.products_details,name='products_details'),
   
] 