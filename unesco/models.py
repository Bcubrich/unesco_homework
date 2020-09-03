from django.db import models


class Category(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class States(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=2,null=True)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description =models.CharField(max_length=2000,null=True)
    justification =models.CharField(max_length=2000,null=True)
    longitude =models.FloatField(max_length=20,null=True)
    latitude =models.FloatField(max_length=20,null=True)
    area_hectares =models.FloatField(max_length=20,null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE,null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE,null=True)


    def __str__(self) :
        return self.name