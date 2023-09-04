from django.contrib.auth import views as auth_views
from reservation import views
from django.urls import path
from .views import LoginView, SignupView


app_name = 'reservation'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('view/', views.IndexReservation.as_view(), name='view'),
    path('information/', views.InformationView.as_view(), name='information'),
    path('create/', views.CreateReservation.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateReservation.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteReservation.as_view(), name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('signup/', views.SignupView, name='signup'),
]
