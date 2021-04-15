from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='bus'),
    path('routes', views.routes, name='routes'),
    path('flights', views.flights, name='flights'),
    path('login', views.loginView, name='login'),
    path('logout', LogoutView.as_view(next_page="/"),name='logout'),
    path('busForm', views.busForm, name='addBus'),
    path('busForm/<int:id_bus>', views.busForm, name='updateBus'),
    path('routeForm', views.routeForm, name='addRoute'),
    path('routeForm/<int:id_route>', views.routeForm, name='updateRoute'),
    path('flightForm', views.flightForm, name='addFlight'),
    path('flightForm/<int:id_flight>', views.flightForm, name='updateFlight'),
    path('delBus/<int:id_bus>/', views.delBus, name='delBus'),
    path('delRoute/<int:id_route>/', views.delRoute, name='delRoute'),
    path('delFlight/<int:id_flight>/', views.delFlight, name='delFlight'),
]
