from django.db import models

# Create your models here.

class penerima(models.Model):
    nama = models.CharField(max_length=100)
    telepon = models.CharField(max_length=12)
    alamat = models.TextField(max_length=500)
    kodepos = models.IntegerField()

    def __str__(self):
        return self.nama

class pengirim(models.Model):
    nama = models.CharField(max_length=100)
    telepon = models.CharField(max_length=12)
    alamat = models.TextField(max_length=500)
    kodepos = models.IntegerField()
    penerima = models.ForeignKey(penerima, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama
    
