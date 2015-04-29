from django.db import models
from djangotoolbox.fields import ListField
from django_mongodb_engine.contrib import MongoDBManager
from djangotoolbox.fields import EmbeddedModelField


# class User(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     comment = models.CharField(max_length=10000)
#
#     def __unicode__(self):
#         return self.name
#
#     def header(self):
#         return {"id": "id", "name": "name", "comment": "comment"}
#
#     def dictionary(self):
#         return {"id": self.name, "name": self.name, "comment": self.comment}
#
#
# class Bill(models.Model):
#     amount = models.FloatField()
#     average_amount_for_month = models.FloatField()
#
#     def __unicode__(self):
#         return str(self.amount)
#
#     def header(self):
#         return {"amount": "amount", "average_amount_for_month": "average_amount_for_month"}
#
#     def dictionary(self):
#         return {"amount": self.amount, "average_amount_for_month": self.average_amount_for_month}
#
#
# class Time(models.Model):
#     datetime = models.DateTimeField(auto_now_add=True)
#     at_day_time = models.BooleanField(default=False)
#
#     def __unicode__(self):
#         return str(self.datetime)
#
#     def header(self):
#         return {"datetime": "datetime", "at_day_time": "at_day_time"}
#
#     def dictionary(self):
#         return {"datetime": self.datetime, "at_day_time": self.at_day_time}


class Transaction(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    name = models.CharField(max_length=100)
    bill = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    objects = MongoDBManager()