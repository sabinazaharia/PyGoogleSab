from django.db import models

tipuri_companie = (('SRL', 'S.R.L'), ('SC', 'S.C'), ('SA', 'S.A'))



class Companies(models.Models):
    nume = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    tip_companie = models.CharField(max_length=10, choices=tipuri_companie)

    def __str__(self):
        return f"{self.nume} - {self.tip_companie}"