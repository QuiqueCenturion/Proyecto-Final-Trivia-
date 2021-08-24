from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import render

# Create your views here.

'''User views'''

# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def ingreso(request):
    if request.method == "POST":
        print("*"*10)
        username = request.POST["username"] 
        password = request.POST["password"] 
        user = authenticate(request, username=username, password=password)
        print(username, ":", password)
        print("*"*10)

        if user:
            login(request, user)
            return redirect("https://www.youtube.com")
        else:
            return render(request,"ingreso.html",{"error":"Usuario o contraseña invalida"})

        
    return render(request,"ingreso.html")