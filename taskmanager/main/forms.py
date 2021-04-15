from django.contrib.auth import forms
from django.contrib.auth.models import User

from .models import Bus, Route, Flight
from django.forms import ModelForm, TextInput, DateTimeInput, Select, DateInput, EmailInput, PasswordInput, NumberInput
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ("board_number", "regist_number", "number_of_places", "mark")
        labels = {
            "board_number": 'Бортовый номер',
            "regist_number": 'Регистрационный номер',
            "number_of_places": 'Число мест',
            "mark": 'Марка'
        }
        widgets = {
            "board_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите бортовой номер'
            }),
            "regist_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите регистрационный номер'
            }),
            "number_of_places": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество мест'
            }),
            "mark": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите марку автобуса'
            })
        }


class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ("route_number",
                  "stop_from_address",
                  "stop_to_address",
                  )
        labels = {
            "route_number": 'Номер маршрута',
            "stop_from_address": 'Пункт отправления',
            "stop_to_address": 'Пункт назначения'
        }
        widgets = {
            "route_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер маршрута'
            }),
            "stop_from_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "stop_to_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            })
        }


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = ("flight_num",
                  "driver",
                  "id_bus",
                  "id_route",
                  "ticket_price",
                  "departure_time",
                  "arrival_time",
                  )
        labels = {
            "flight_num": 'Номер рейса',
            "driver": 'ФИО Водителя',
            "id_bus": 'Автобус',
            "id_route": 'Маршрут',
            "ticket_price": 'Цена',
            "departure_time": 'Время отправления',
            "arrival_time": 'Время прибытия'
        }
        widgets = {
            "flight_num": TextInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Введите номер рейса'
            }),
            "driver": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО водителя'
            }),
            "id_bus": Select(attrs={
                'class': 'form-select ' ,
                'placeholder': 'Введите ФИО водителя'
            }),
            "id_route": Select(attrs={
                'class': 'form-select',
                'placeholder': 'Введите ФИО водителя'
            }),

            "ticket_price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            },

            ),

            "departure_time": DateInput(attrs={'type': 'datetime-local',
                                             'class': 'form-control'},
                                        format='%H:%M'),

            "arrival_time": DateInput(attrs={'type': 'datetime-local',
                                             'class': 'form-control'},
                                      format='%H:%M',)
        }

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.fields['id_bus'].empty_label = "Выбрать"
        self.fields['id_route'].empty_label = "Выбрать"


class LoginForm(ModelForm):
    captcha = ReCaptchaField()


    class Meta:
        model = User
        fields = ("username", "password", "captcha")
        labels = {
            "username": 'Имя пользователя',
            "password": 'Пароль'
        }
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с именем {username} не найден в системе.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data
