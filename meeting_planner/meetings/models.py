from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()
    # block
    # google_pin
    # capacity = models.IntegerField(default=2)

    def __str__(self):
        return f'{self.name}: room {self.room_number} on floor {self.floor_number}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    # end_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} at {self.start_time} on {self.date}'
