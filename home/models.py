from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ', ' + self.address


class Individual(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    is_married = models.BooleanField(default=False)

    def __str__(self):
        return str(self.age) + ' years old ' + self.gender + ', ' + self.nationality
