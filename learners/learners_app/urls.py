from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('login_page', views.login_page,name='login_page'),#Login_page
    path('home_page', views.home_page, name='home_page'),  # Home_page
    path('logout_page', views.login_page, name='logout_page'),  # Logout_page
    path('first_page', views.first_page, name='first_page'),  # first_page
    path('registration_page', views.registration_page, name='registration_page'),  # registraion_page
    path('user_add', views.user_add, name='user_add'),  # user_add
    path('user_update/<int:user_id>/', views.user_add, name='user_update'),  # user_update
    path('user_delete/<int:user_id>/', views.user_delete, name='user_delete'),  # user_delete
    path('user_list', views.user_list, name='user_list'),  # user_list
    path('user_list_temp', views.user_list_temp, name='user_list_temp'),  # user_list
]