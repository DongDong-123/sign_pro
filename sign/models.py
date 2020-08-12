from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=30)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=128)
    start_time = models.DateTimeField('events time')  # events time,后台管理中显示为字段名
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event", "phone")  # 设置两个字段为联合主键
        ordering = ['id']
    def __str__(self):
        return self.real_name
