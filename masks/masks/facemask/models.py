from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class SupportModel(models.Model):
    usuario = models.CharField(max_length=30)
    asunto = models.CharField(max_length=100)
    comment = models.TextField()

class MaskCreator(models.Model):
    # telas
    ALG = "Algodón"
    POL = "Poliéster"
    FRA = "Franela"
    SBN = "Sábana"
    FABR_CHOICES = [(ALG,"Algodón"),(POL,"Poliéster"),(FRA,"Franela"),(SBN,"Sábana")]
    # colores
    AZU = "Azul"
    NEG = "Negro"
    ROJ = "Rojo"
    BLA = "Blanco"
    GRI = "Gris"
    ROS = "Rosa"
    CAF = "Cafe"
    COL_CHOICES = [(AZU,"Azul"),(NEG,"Negro"),(ROJ,"Rojo"),
                (BLA,"Blanco"),(GRI,"Gris"),(ROS,"Rosa"),(CAF,"Cafe")]
    usuario = models.CharField(max_length=30)
    tela = models.CharField(max_length=20,choices=FABR_CHOICES)
    color = models.CharField(max_length=20,choices=COL_CHOICES,default=BLA)
    capas = models.IntegerField(default=2,validators=[MinValueValidator(1),MaxValueValidator(4)])

class BrandMasks(models.Model):
    INF = "Infantil"
    SPT = "Deportes"
    CAS = "Casual"
    RAR = "Raro"
    TYPE_CHOICES = [
    (INF, "Infantil"), (SPT,"Deportes"),
     (CAS,"Casual"), (RAR, "Raro")]
    marca = models.CharField(max_length=50)
    enlace = models.CharField(max_length=300)
    photo = models.CharField(max_length=300)
    category = models.CharField(max_length=15,choices=TYPE_CHOICES)
    price = models.FloatField(default=5.0,validators=[
            MaxValueValidator(500),
            MinValueValidator(5.0)
    ])
