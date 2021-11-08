from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # Creamos las rutas para publicar los end
    path('', include('products.urls'))
]
