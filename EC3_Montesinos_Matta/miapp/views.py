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