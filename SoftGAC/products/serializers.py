# se importa la utilidad serializers de rest_framework
from rest_framework import serializers
# importamos tambien el modelo o modelos que deseamos transformar
from .models import Product

# Creamos la clase para serializar el modelo 

class ProductSerializer(serializers.ModelSerializer):
  nombre = serializers.CharField(max_length=20,required=True)
  precio = serializers.IntegerField(required=True)

  def create(self, validated_data):
    # Una vez los datos solicitados han sido validados,
    # podemos crear una instancia de un producto en
    # la base de datos
    return Product.objects.create(
      nombre = validated_data.get('nombre'),
      precio = validated_data.get('precio'),
    )

  def update(self, instance, validated_data):
    # Una vez los datos han sido validados,
    # podemos actualizar una instancia del producto en base de datos
    instance.nombre = validated_data.get('nombre', instance.nombre)
    instance.save()
    instance.precio = validated_data.get('precio', instance.nombre)
    instance.save()
    return instance

  class Meta:
    model = Product
    fields = [ 
      'id', 
      'nombre', 
      'precio', 
      'categoria', 
      'dimensiones', 
      'referencia', 
      'foto' 
    ]
