from django.http import HttpResponse
from zeep import Client
from django.template import loader
from formularios import  realizarJugadaLoto
from django.views.decorators.csrf import csrf_exempt

from formularios import realizarJugadaPale

wsdl = 'http://localhost:7777/ws/LoteriaWebServices?wsdl'
client = Client(wsdl = wsdl)
#print(client.service.prueba())

@csrf_exempt
def jugarPale(request):
    gan = False
    template = loader.get_template("jugadaPale.html")
    template2 = loader.get_template("resultado.html")
    if request.method == 'POST':
        form = realizarJugadaPale(request.POST)
        Usuario = form.data.get('usuario')
        Clave = form.data.get('clave')
        Monto = form.data.get('monto')
        Primero = form.data.get('primero')
        Segundo = form.data.get('segundo')
        Tercero = form.data.get('tercero')
        Ganar = form.data.get('ganar')
        if Ganar == 'on':
            gan = True
        resultado = client.service.jugarPale(Monto, Primero, Segundo, Tercero, Usuario, Clave, gan)
        return HttpResponse(template2.render({'resultado' : resultado}), request)

    elif request.method == 'GET':
        form = realizarJugadaPale()

    return HttpResponse(template.render({'form' : form}), request)

@csrf_exempt
def jugarLoto(request):
    gan = False
    template = loader.get_template("jugadaLoto.html")
    template2 = loader.get_template("resultado.html")
    if request.method == 'POST':
        form = realizarJugadaLoto(request.POST)
        Usuario = form.data.get('usuario')
        Clave = form.data.get('clave')
        Primero = form.data.get('primero')
        Segundo = form.data.get('segundo')
        Tercero = form.data.get('tercero')
        Cuarto = form.data.get('cuarto')
        Quinto = form.data.get('quinto')
        Ganar = form.data.get('ganar')
        if Ganar == 'on':
            gan = True
        #(int Primero, int Segundo, int Tercero, int Cuarto, int Quinto, String usuario, String clave, boolean ganador)
        resultado = client.service.jugarLoto(Primero, Segundo, Tercero, Cuarto, Quinto, Usuario, Clave, gan)
        return HttpResponse(template2.render({'resultado' : resultado}), request)

    elif request.method == 'GET':
        form = realizarJugadaLoto()

    return HttpResponse(template.render({'form' : form}), request)