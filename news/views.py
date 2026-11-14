from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
"""
def home(request):
    return HttpResponse("<h1>Homepage news!</h1>")
    #restituisce solo la scritta
""" 


"""
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a+=art.titolo+"<br>"

    for gio in Giornalista.objects.all():
        g+=gio.nome+" "+gio.cognome+"<br>"

    reponse= "Articoli: <br>"+a+"<br>Giornalisti: <br>"+g

    return HttpResponse("<h1>"+reponse+"</h1>")
    #restituisce come print
"""

"""def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    reponse= str(a)+"<br>"+str(g)
    print(reponse)

    return HttpResponse("<h1>"+reponse+"</h1>")
    #printa la lista
"""

def home(request):
    articoli= Articolo.objects.all()
    giornalisti=Giornalista.objects.all()

    context = {
        'articoli': articoli,
        'giornalisti': giornalisti
    }
    print(context)
    return render(request, 'home.html', context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {
        'articolo': articolo
    }
    return render(request, 'articolo_detail.html', context)