"""
Models representing database
"""
from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    name = models.TextField()
    surname = models.TextField()
    birthid = models.CharField(max_length=15)
    email = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class HygienicStation(models.Model):
    address = models.TextField()
    manager = models.TextField()

    def __str__(self):
        return self.address


class Facility(models.Model):
    address = models.TextField()


class Place(models.Model):
    bed = models.TextField()
    standard = models.TextField(blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)


class Quarantine(models.Model):
    startdate = models.DateField()
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


class CovidTest(models.Model):
    waitdays = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.TextField()

    def __str__(self):
        return self.type


class CovidPass(models.Model):
    TEST_RESULTS = [
        ('POS', 'Positive'),
        ('NEG', 'Negative')
    ]
    testresult = models.CharField(max_length=3, choices=TEST_RESULTS, blank=True)
    testdate = models.DateField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hygienicstation = models.ForeignKey(HygienicStation, on_delete=models.CASCADE, null=True, blank=True)
    covidtest = models.ForeignKey(CovidTest, on_delete=models.CASCADE, null=True)


class Reservation(models.Model):
    createdate = models.DateTimeField()
    deadline = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    covidpass = models.ForeignKey(CovidPass, on_delete=models.CASCADE, null=True)


class Administrative(models.Model):
    name = models.TextField()
    surname = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Doctor(models.Model):
    name = models.TextField()
    surname = models.TextField()
    title = models.CharField(max_length=5, blank=True)
    address = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
