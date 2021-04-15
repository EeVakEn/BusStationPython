from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import BusForm, RouteForm, FlightForm, LoginForm
from .models import Bus, Route, Flight


def index(request):
    buses = Bus.objects.all()
    return render(request, 'main/index.html', {'title': 'Автобусы', 'buses': buses})


def routes(request):
    routes = Route.objects.all()
    return render(request, 'main/routes.html', {'title': 'Маршруты', 'routes': routes})


def flights(request):
    flights = Flight.objects.all()
    return render(request, 'main/flights.html', {'title': 'Рейсы', 'flights': flights})


def loginView(request):
    if request.method == "GET":
        form = LoginForm(request.POST or None)
        return render(request, 'main/login.html', {'form': form})

    else:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'main/login.html', {'form': form})



def busForm(request, id_bus=0):
    if request.method == "GET":  # получение странички

        # insert
        if id_bus == 0:
            form = BusForm()  # возврат пустой формы
            title = 'Добавить автобус'
        # update
        else:
            title = 'Измененить автобус'
            bus = Bus.objects.get(pk=id_bus)
            form = BusForm(instance=bus)  # возврат заполненной формы

        return render(request, "main/busForm.html", {'form': form, 'title': title})
    else:  # обработка формы
        if id_bus == 0:
            form = BusForm(request.POST)
        else:
            bus = Bus.objects.get(pk=id_bus)
            form = BusForm(request.POST, instance=bus)

        if form.is_valid():
            form.save()
        return redirect('/')


def routeForm(request, id_route=0):
    if request.method == "GET":  # получение странички

        # insert
        if id_route == 0:
            form = RouteForm()  # возврат пустой формы
            title = 'Добавить маршрут'
        # update
        else:
            title = 'Изменить маршрут'
            route = Route.objects.get(pk=id_route)
            form = RouteForm(instance=route)  # возврат заполненной формы

        return render(request, "main/routeForm.html", {'form': form, 'title': title})
    else:  # обработка формы
        if id_route == 0:
            form = RouteForm(request.POST)
        else:
            route = Route.objects.get(pk=id_route)
            form = RouteForm(request.POST, instance=route)

        if form.is_valid():
            form.save()
        return redirect('/routes')


def flightForm(request, id_flight=0):
    if request.method == "GET":  # получение странички

        # insert
        if id_flight == 0:
            form = FlightForm()  # возврат пустой формы
            title = 'Добавить рейс'
        # update
        else:
            title = 'Изменить рейс'
            flight = Flight.objects.get(pk=id_flight)
            form = FlightForm(instance=flight)  # возврат заполненной формы

        return render(request, "main/flightForm.html", {'form': form, 'title': title})
    else:  # обработка формы
        if id_flight == 0:
            form = FlightForm(request.POST)
        else:
            flight = Flight.objects.get(pk=id_flight)
            form = FlightForm(request.POST, instance=flight)

        if form.is_valid():
            form.save()
        return redirect('/flights')


def delBus(request, id_bus):
    if request.method == 'POST':
        bus = Bus.objects.get(id=id_bus)
        bus.delete()
    return redirect('/')


def delRoute(request, id_route):
    if request.method == 'POST':
        route = Route.objects.get(id=id_route)
        route.delete()
    return redirect('/routes')


def delFlight(request, id_flight):
    if request.method == 'POST':
        flight = Flight.objects.get(id=id_flight)
        flight.delete()
    return redirect('/flights')
