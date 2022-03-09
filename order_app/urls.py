from django.urls import path
from .views import *

urlpatterns = [
   
    path('',index,name='index'),
    path('order/',order,name='order'),
    path('orders/',orders,name='orders'),
    path('delete/<int:id>/',delete,name='delete'),
    #path('edit/<int:id>/',edit,name='edit'),
    path('update/<int:id>/',update,name='update'),
]