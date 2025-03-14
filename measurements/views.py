from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os

# Importar lógica de mediciones
from .forms import MeasurementForm
from django.contrib import messages
from .logic.logic_measurement import create_measurement, get_measurements

# ✅ Función para listar mediciones
def measurement_list(request):
    measurements = get_measurements()
    context = {
        'measurement_list': measurements
    }
    return render(request, 'Measurement/measurements.html', context)

# ✅ Función para crear una medición
def measurement_create(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            create_measurement(form)
            messages.add_message(request, messages.SUCCESS, 'Measurement created successfully')
            return HttpResponseRedirect(reverse('measurementCreate'))
        else:
            print(form.errors)
    else:
        form = MeasurementForm()
    return render(request, 'Measurement/measurementForm.html', {'form': form})

# ✅ Endpoint para subir archivos EEG
@csrf_exempt
def upload_eeg(request):
    if request.method == 'POST' and request.FILES.get('eeg_file'):
        eeg_file = request.FILES['eeg_file']
        file_path = os.path.join('uploads', eeg_file.name)
        
        # Guardar el archivo en el servidor
        saved_path = default_storage.save(file_path, eeg_file)
        
        # Simulación del procesamiento del EEG (esto se debe reemplazar con análisis real)
        result = {
            "file": eeg_file.name,
            "status": "Processed Successfully",
            "diagnosis": "No abnormal activity detected"
        }
        
        return JsonResponse(result)

    return JsonResponse({"error": "Invalid request"}, status=400)
