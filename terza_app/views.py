from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"terza_app/index.html")

def view_a(request):
    'var1' : randomRandint(1,11),
    'var2' : randomRandint(1,11),
    return render(request, "terza_app/view_a.html", var1,var2)

def view_b(request):
    lista=[]
    for _ in range(30):
        lista.append(randomRandint(1,11))

    return render(request,"terza_app/view_b.html", lista)

def view_c(request):
    dic = { 
        'Milano': 18,
        'Roma': 20,
        'Torino': 16,
        'Catanzaro': 21,
        'Soverato': 15,
    }
    return render(request,"terza_app/view_c.html",dic)