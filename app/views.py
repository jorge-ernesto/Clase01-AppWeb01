from django.shortcuts import render,HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse('Hola alumnos desde Django!')

def index(request):
    documento=''' 
    <html>
    <body>
    <h1>mi primera pagina web con Django </h1>
    </body>
    </html>
    '''
    return HttpResponse(documento)
