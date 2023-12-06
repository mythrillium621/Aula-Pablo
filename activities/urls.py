from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('new/', views.activity_new, name='activity_new'),
    path('<int:id>/edit/', views.activity_edit, name='activity_edit'),
    path('<int:id>/delete/', views.activity_delete, name='activity_delete'),
]