from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del panel de administración

    # ✅ Incluir las rutas de las apps
    path('', include('measurements.urls')),  # Rutas de measurements
    path('', include('variables.urls')),  # Rutas de variables
]

