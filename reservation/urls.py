from reservation import views
from django.urls import path


app_name = 'reservation'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('view/', views.IndexReservation.as_view(), name='view'),
    path('create/', views.CreateReservation.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateReservation.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteReservation.as_view(), name='delete')
]