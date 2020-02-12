from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:class_id>/', views.detail, name='class_detail'),
    path('check-in/<int:class_id>/', views.check_in, name='class_check_in'),
]