from django.shortcuts import render

def pengirim(request):
    return render(request, 'jago/pengirim.html',)

def penerima(request):
    return render(request, 'jago/penerima.html',)
