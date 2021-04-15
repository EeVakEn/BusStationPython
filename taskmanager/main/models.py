from django.db import models


# Create your models here.


class Bus(models.Model):
    board_number = models.CharField('Бортовый номер', max_length=50)
    regist_number = models.CharField('Регистрационный номер', max_length=9)
    number_of_places = models.IntegerField('Число мест')
    mark = models.CharField('Марка', max_length=50)

    def __str__(self):
        return self.regist_number + ' ' + self.mark


class Route(models.Model):
    route_number = models.CharField('Номер маршрута', max_length=9)
    stop_from_address = models.CharField('Пункт отправки', max_length=50)
    stop_to_address = models.CharField('Пункт назначения', max_length=50)
    def __str__(self):
        return self.stop_from_address + ' ' + self.stop_to_address


class Flight(models.Model):
    flight_num = models.CharField('Номер рейса', max_length=20)
    driver = models.CharField('Имя водителя', max_length=50)
    id_bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    ticket_price = models.IntegerField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.flight_num



