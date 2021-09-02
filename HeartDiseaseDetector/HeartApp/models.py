from django.db import models

# Create your models here.

class Heart(models.Model):

    #class attributes
    patient_id = models.AutoField
    fullname = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=100, default="")

    # Independent feature
    age = models.IntegerField(default="")
    sex = models.IntegerField(default="")
    cp = models.IntegerField(default="")
    trestbps = models.IntegerField(default="")
    chol = models.IntegerField(default="")
    fbs = models.IntegerField(default="")
    restecg = models.IntegerField(default="")
    thalach = models.IntegerField(default="")
    exang = models.IntegerField(default="")
    oldpeak = models.FloatField(default="")
    slope = models.IntegerField(default="")
    ca = models.IntegerField(default="")
    thal = models.IntegerField(default="")
    
    # Dependent feature
    target = models.IntegerField(default="")

    def __str__(self) -> str:
        return str(self.patient_name)
