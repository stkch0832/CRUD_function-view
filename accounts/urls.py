from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('regist/', views.regist, name='regist'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/edit', views.profile_edit, name='profile_edit'),
]
