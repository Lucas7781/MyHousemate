from django.db import models
from datetime import datetime

class House(models.Model):
    house_name = models.CharField(max_length = 100)
    house_size = models.IntegerField()
    schedule_type = models.CharField(max_length = 100)
    members = models.ManyToManyField('User')

class User(models.Model):
    name = models.CharField(max_length=100)
    houses = models.ManyToManyField('House')

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    house = models.ForeignKey(House, on_delete=models.CASCADE, default=None)
    task_description = models.CharField(max_length=350, default=None)

    class Meta:
        unique_together = ('task_name', 'house')

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ('user', 'house', 'task')

class Notification(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    send_time = models.DateTimeField(default=datetime.now())