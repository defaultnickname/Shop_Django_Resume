from django.shortcuts import render

# Create your views here.


def index(request):
    context = { }
    return render(request, "index.html",context)

def products(request):
    context = { }
    return render(request, "products.html",context)

def newstuff(request):
    context = { }
    return render(request, "newstuff.html",context)

def discount(request):
    context = { }
    return render(request, "discount.html",context)

def cart(request):
    context = { }
    return render(request,"cart.html", context)

def clothes(request):
    context = { }
    return render(request,"clothes.html", context)

def shoes(request):
    context = { }
    return render(request,"shoes.html", context)

def accesories(request):
    context = { }
    return render(request,"accesories.html", context)

def sport(request):
    context = { }
    return render(request,"sport.html", context)