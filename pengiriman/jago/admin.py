from django.contrib import admin
from jago.models import pengirim, penerima
# Register your models here.

class pengirimAdmin(admin.ModelAdmin):
    list_display = ['nama', 'telepon', 'alamat', 'kodepos']
    search_fields = ['nama', 'alamat']


class penerimaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'telepon', 'alamat', 'kodepos']
    search_fields = ['nama', 'alamat']

admin.site.register(pengirim, pengirimAdmin)
admin.site.register(penerima, penerimaAdmin) 