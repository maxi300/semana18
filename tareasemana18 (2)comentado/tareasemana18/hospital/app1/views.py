from django.shortcuts import render
from .models import Medico, Paciente2
from .formularios import add_medic as fm
from django.http import HttpResponseRedirect

#este es para que cargue la primer vista principal donde estan los botones que dicen que si quiere ver las 
#tablas ya se de paciente
def index(request):
    return render(request,"index.html")


#esta vista carga donde estan los datos de los medicos en tablas
def list_med(request):
    medicos= Medico.objects.all()
    return render(request, "lismed.html",{"lismed":medicos})
# Create your views here.


#esta vista carga donde estan los datos de los pacientes en la tabla
def list_pac(request):
    paciente= Paciente2.objects.all()
    return render(request, "lispa.html",{"lispa":paciente})
# Create your views here.


#aqui se valida el api form y si es correcto entonces almacenamos los datos de las tablas en los campos de los
#modelos
        
def add_pac(request):
    if request.method == "POST":
        formulario = fm.Add_pac(request.POST)
        if formulario.is_valid():
            nuevo_paciente = Paciente2(
                nombre=formulario.cleaned_data["nombre"],
                apellido=formulario.cleaned_data["apellido"],
                fecha_nacimiento=formulario.cleaned_data["cumple"],
                sexo=formulario.cleaned_data["sexo"],
                altura=formulario.cleaned_data["altura"],
                med=formulario.cleaned_data["medico"],
              
            )
            nuevo_paciente.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.Add_pac()
        return render(request, "add_pac.html", {"form": formulario})











    #se aplica lo mismo que la vista anterior
    #con el .save() lo que hace es que lo guarda en el modelo creado
    #y si no pues cargamos la appi del formulario

        
def add_med(request):
    if request.method == "POST":
        formulario = fm.Add_medic(request.POST)
        if formulario.is_valid():
            nuevo_medico = Medico(
                nombre=formulario.cleaned_data["nombre"],
                apellido=formulario.cleaned_data["apellido"],
                especialidad=formulario.cleaned_data["especialidad"]
            )
            nuevo_medico.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.Add_medic()
        return render(request, "Add_medic.html", {"form": formulario})