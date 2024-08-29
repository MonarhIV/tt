from django.db import models


class DataEntry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    timeToCreate = models.DateField()
    timeToResolve = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.timeToCreate}, {self.timeToResolve}, {self.status}'