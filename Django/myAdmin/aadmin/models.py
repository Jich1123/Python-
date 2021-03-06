from django.db import models
import time
# Create your models here.
class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomname = models.CharField(max_length=20)

    def __str__(self):
        return self.roomname

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)

    room = models.OneToOneField(ClassRoom)

    def getRoomName(self):
        return self.room.roomname

    getRoomName.short_description = "所在教师"

    def curTime(self):
        return time.time()

    curTime.short_description = "当前时间"
    curTime.admin_order_field = "name"
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom)
    def __str__(self):
        return self.name