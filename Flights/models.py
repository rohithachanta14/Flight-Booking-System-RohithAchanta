from django.db import models

class Airline(models.Model):
    airline_name=models.CharField(max_length=20)
    def __str__(self):
        return self.airline_name
class Availability(models.Model):
    airline=models.ForeignKey(Airline,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    src=models.CharField(max_length=100)
    dest=models.CharField(max_length=100)
    seatsavail=models.IntegerField()
