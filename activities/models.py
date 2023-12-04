from django.db import models

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    hours_spent = models.IntegerField()
    minutes_spent = models.IntegerField()

    def __str__(self):
        return self.name