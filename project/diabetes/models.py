from django.db import models


class DiabetespredictionModel(models.Model):
    Pregnancies=models.IntegerField()
    Glucose=models.IntegerField()
    BloodPressure=models.IntegerField()
    SkinThickness=models.IntegerField()
    Insulin=models.IntegerField()
    BMI=models.DecimalField(decimal_places=4,max_digits=7)
    DiabetesPedigreeFunction=models.DecimalField(decimal_places=5,max_digits=5)
    age=models.IntegerField()


