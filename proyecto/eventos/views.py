from django.shortcuts import render, HttpResponse

def eventos(request):
    return render(request, "evento/eventos.html")