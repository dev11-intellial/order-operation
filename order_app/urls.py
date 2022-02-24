from django.urls import path
from .views import *

urlpatterns = [
   
    path('',index,name='index'),
    path('create_order/',create_order,name='create_order'),
    path('all_order/',all_order,name='all_order'),
    path('delete/<int:id>/',delete,name='delete'),
    path('edit/<int:id>/',edit,name='edit'),
    path('update/<int:id>/',update,name='update'),
]