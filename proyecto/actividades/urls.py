from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "actividades"
urlpatterns = [

#---------------------ACTAS MATRIMONIALES------------------------    
    path('actividad/', views.actividads, name="activi"),
    path('actas_agregar/', views.agregar_acta, name="actas"),
    path('actas_listar/', views.listar_acta, name="actas_lista"),
    path('listar_nuevos/', views.list_programmers, name="list_progra"),





# ---------------------ACTIVIDADES EDUCATIVAS-------------------
    path('agregar_actividad/', views.agregar_actividad, name="agregar_act"),
    path('listar/', views.listar_miem, name="lista"),
    


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)