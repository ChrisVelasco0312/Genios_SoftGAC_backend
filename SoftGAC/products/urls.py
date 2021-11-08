from django.urls import path
# Importamos las vistas
from . import views

urlpatterns = [
    # Creamos las rutas para publicar los end
    path('products/', views.ProductListView.as_view()),
    path('products/<int:id>', views.ProductListView.as_view()),
]
