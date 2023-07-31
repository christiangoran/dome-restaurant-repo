from . import views
from django.urls import path


app_name = 'reservation'
urlpatterns = [
    path('', views.IndexReservation.as_view(), name='home'),
    path('<int:pk>/', views.DetailReservation.as_view(), name='detail'),
]