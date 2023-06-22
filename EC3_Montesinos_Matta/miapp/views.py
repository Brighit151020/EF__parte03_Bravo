from django.shortcuts import render, HttpResponse,redirect

def index(request):
    curso = [ 'Dinamica de Sistemas',
'LP3',
'Microoprocesadores',
'Gestión de Procesos',
'Algoritmos de computación gráfica',
'Ingernieria de requerimientos',
'Hacking']
   

    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web con Django',
        'cursos':curso
})


def rango(request):
    a = 5
    b = 100
    
    rango_numeros = []
    
    for num in range(a, b+1):
        if num > 1:  # Los números primos son mayores que 1
            es_primo = True
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                rango_numeros.append(num)
    
    return render(request, 'rango.html', {
        'titulo': 'Rango',
        'a': a,
        'b': b,
        'rango_numeros': rango_numeros
    })