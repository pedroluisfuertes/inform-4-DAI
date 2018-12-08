from django.db import models
from django.utils import timezone
from pymongo import MongoClient
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

client = MongoClient()
db = client.test                  # base de datos
restaurantes = db.restaurants     # colección

class Plato(models.Model):
    ITALIANA = 'italiana'
    VEGETARIANA = 'vegetariana'
    ESPANOA = 'Española'
    TIPOS_COCINAS = (
        (ITALIANA, 'italiana'),
        (VEGETARIANA, 'vegetariana'),
        (ESPANOA, 'Española'),
    )
    ALERGENOS = (())

    nombre = models.TextField(max_length = 200, blank = False) 
    precio = models.DecimalField(max_digits = 5,decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], blank = False)
    tiposCocinas = models.CharField(choices=TIPOS_COCINAS, default=ESPANOA,max_length=100)
    alergenos = models.CharField(choices=ALERGENOS, default=ESPANOA,max_length=100)
    descripcion = models.TextField(max_length = 500)

    def insertar(self):
        self.precio = 0
        self.save()

    def eliminar(self):
        self.precio = 0

    def modificar(self):
        self.precio = 0
    
    def __str__(self):
        return self.nombre

        from django.db import models

