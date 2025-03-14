from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views  # ✅ Importar views correctamente
from measurements.views import upload_eeg  # ✅ Importar la función específica

urlpatterns = [
    path('measurements/', views.measurement_list, name='measurement_list'),
    path('measurementcreate/', csrf_exempt(views.measurement_create), name='measurementCreate'),

    # ✅ Nuevo endpoint para la carga de EEG
    path('upload-eeg/', upload_eeg, name='upload-eeg'),
]
