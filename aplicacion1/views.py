from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def Consulta(request):
    return render(request,"Consulta.html")

def Dashboard(request):
    return render(request,"Dashboard.html")
