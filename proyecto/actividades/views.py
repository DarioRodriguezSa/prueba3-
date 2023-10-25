from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import actividad, categoria, curso, clase,status, miembro, maestro
from actividades.models import acta
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

@login_required(login_url="auth/login/")
def actividads(request):
    return render(request, "actividad/actividades.html")



@login_required(login_url="auth/login/")
def agregar_actividad(request):
    categorias = categoria.objects.all()
    clases = clase.objects.all()
    miembros = miembro.objects.all()
    cursos = curso.objects.all()
    statuses = status.objects.all()
    maestros = maestro.objects.all()

    if request.method == 'POST':
        data = request.POST
        try:
            categoria_obj = categoria.objects.get(pk=data['categoria'])
            clase_obj = clase.objects.get(pk=data['clase'])
            miembro_obj = miembro.objects.get(pk=data['miembro'])
            maestro_obj = maestro.objects.get(pk=data['maestro'])
            curso_obj = curso.objects.get(pk=data['curso'])
            status_obj = status.objects.get(pk=data['status'])


            nueva_actividad = actividad(
                categoria=categoria_obj,
                clase=clase_obj,
                miembroa=miembro_obj,
                maestro=maestro_obj,
                curso=curso_obj,
                status=status_obj,
                fechainicio=data['fechainicio'],
                duracion=data['duracion'],
                fechafin=data['fechafin']
            )
            nueva_actividad.save()

            messages.success(request, 'Actividad creada con éxito!', extra_tags="success")
            return redirect('actividades:agregar_act')

        except Exception as e:
            messages.error(request, 'Error al crear la actividad: ' + str(e), extra_tags="danger")
            return redirect('actividades:agregar_act')

    return render(request, "actividad/agregar_actividad.html", {
        'categorias': categorias,
        'clases': clases,
        'miembros': miembros,
        'cursos': cursos,
        'statuses': statuses,
        'maestros': maestros,
    })




@login_required(login_url="auth/login/")
def listar_miem(request):
    query = request.GET.get('q', '')

    # Imprimir el valor de query en la consola o en el registro
    print("Valor de query:", query)

    miembros = miembro.objects.filter(
        Q(nombre__icontains=query) |
        Q(apellido__icontains=query) |
        Q(genero__nombre__icontains=query) |
        Q(nacionalidad__nombre__icontains=query) |
        Q(edad__icontains=query)
    )

    if query.isdigit():
        miembros = miembros.filter(edad=int(query))
    context = {
        "active_icon": "miembros",
        "miembros": miembros,
        "query": query,
    }
    return render(request, "actividad/agregar_actividad.html", context)










@login_required(login_url="auth/login/")
def listar_acta(request):
    return render(request, "actividad/listar_actas.html")

def list_programmers(request):
    programmers=list(acta.objects.values())
    data={'programmers':programmers}
    return JsonResponse(data)



@login_required(login_url="auth/login/")
def agregar_acta(request):
    if request.method == 'POST':
        try:
            titulo = request.POST['titulo']
            novio = request.POST['novio']
            novia = request.POST['novia']

            # Validar si ya existe un acta con el mismo título
            if acta.objects.filter(titulo=titulo).exists():
                messages.error(request, 'Ya existe un acta con el mismo título.', extra_tags="danger")
                return redirect('actividades:actas')

            # Validar si ya existe un acta con el mismo novio
            if acta.objects.filter(novio=novio).exists():
                messages.error(request, 'Ya existe un acta con el mismo novio.', extra_tags="danger")
                return redirect('actividades:actas')

            # Validar si ya existe un acta con la misma novia
            if acta.objects.filter(novia=novia).exists():
                messages.error(request, 'Ya existe un acta con la misma novia.', extra_tags="danger")
                return redirect('actividades:actas')

            fecha = request.POST['fecha']
            sheij = request.POST['sheij']
            guardian = request.POST['guardian']
            testigos = request.POST['testigos']

            nueva_acta = acta(
                titulo=titulo,
                fecha=fecha,
                sheij=sheij,
                novio=novio,
                novia=novia,
                guardian=guardian,
                testigos=testigos
            )

            nueva_acta.save()

            messages.success(request, 'Acta creada con éxito!', extra_tags="success")
            return redirect('actividades:actas_lista')
        except Exception as e:
            messages.error(request, 'Error al crear el acta: ' + str(e), extra_tags="danger")
            return redirect('actividades:actas')

    return render(request, "actividad/agregar_acta.html")
