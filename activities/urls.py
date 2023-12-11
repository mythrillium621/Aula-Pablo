from django.urls import path
from . import views
from activities.views import ActivityDelete

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('new/', views.activity_new, name='activity_new'),
    path('<int:id>/edit/', views.activity_edit, name='activity_edit'),
    path('delete/<int:pk>', ActivityDelete.as_view(), name='activity_delete'),
]