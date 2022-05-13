from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request,"app/Home.html")

def Servicios(request):
    return render(request,"app/Servicios.html")  

def Discipulado(request):
    return render(request,"app/Discipulado.html") 

def Libros(request):
    return render(request,"app/Libros.html")  

def Biblias(request):
    return render(request,"app/Biblias.html")        

def Galeria(request):
    return render(request,"app/Galeria.html")

def Contacto(request):
    return render(request,"app/Contacto.html")         