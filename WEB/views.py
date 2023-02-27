from django.shortcuts import render

# Create your views here.

def INICIO (request):
    return render (request,'inicio.html')

def EJERCICIOS (request):
    return render (request,'ejercicios.html')

def CONTACTOS (request):
    return render (request,'contactos.html')

def EJERCICIOS (request,*cadena,**cadenaID):
    #Ejercicio1
    productos = ['Camiseta','gaseosa', 'Zapatos', 'Gorra']
    cantidad_productos = 0
    while True:
        if cantidad_productos >= len(productos):
            break
        else:
            cantidad_productos += 1
            
    #Ejercicio2
    i = 1
    producto = 1
    while i <= 10:
        producto *= i
        i += 1

    #Ejercicio3
    numero = 25
    while True:
        if numero > 0:
            resultado = 'positivo'
            break
        elif numero < 0:
            resultado = 'negativo'
            break
        else:
            resultado = 'cero'
            break
    
    #Ejercicio4
    impares = 0
    for i in range(1, 20, 2):
        impares += i

    
    return render(request,'ejercicios.html',
                  {'producto':producto, 
                   'cantidad_productos':str(cantidad_productos),
                   'resultado':resultado, 'impares':impares})