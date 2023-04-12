from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.new_post, name='new_post'),
    path('<int:pk>/delete', views.post_delete, name='post_delete'),
]
