from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")

def quem_somos(request):
    return render(request, "quemsomos.html")

def servicos(request):
    return render(request, "servicos.html")

def medicamentos(request):
    return render(request, "medicamentos.html")