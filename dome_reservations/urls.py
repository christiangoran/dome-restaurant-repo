from django.contrib import admin
from django.urls import path, include
from reservation.views import CreateReservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservation.urls')),
    path('accounts/', include('allauth.urls')),
]
