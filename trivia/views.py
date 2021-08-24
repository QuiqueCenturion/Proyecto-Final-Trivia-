from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    return render(request,"base.html",{})

def ingreso(request):
    return render(request,"ingreso.html",{})

def comojugar(request):
    return render(request,"comojugar.html",{})

def registro(request):
    return render(request,"registro.html",{})