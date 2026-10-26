from django.shortcuts import render

# Create your views here.
def index_root(request):
    return render(request,"index_root.html")

def prima_app(request):
    return render(request,"prima_app.html")

def seconda_app(request):
    return render(request,"seconda_app.html")

def terza_app(request):
    return render(request,"terza_app.html")

