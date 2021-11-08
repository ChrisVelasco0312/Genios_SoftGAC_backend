# se importa la utilidad serializers de rest_framework
from rest_framework import serializers
# importamos tambien el modelo o modelos que deseamos transformar
from .models import Product

# Creamos la clase para serializar el modelo 

class ProductSerializer(serializers.ModelSerializer):
  nombre = serializers.CharField(max_length=20,required=True)
  precio = serializers.IntegerField(required=True)
  descripcion = serializers.CharField(max_length=1000)
  categoria = serializers.CharField(max_length=20, required=True)
  dimensiones = serializers.CharField(max_length=20, required=True)
  referencia = serializers.CharField(max_length=1000)
  foto = serializers.CharField(max_length=256, required=True)

  def create(self, validated_data):
    # Una vez los datos solicitados han sido validados,
    # podemos crear una instancia de un producto en
    # la base de datos
    return Product.objects.create(
      nombre = validated_data.get('nombre'),
      precio = validated_data.get('precio'),
      descripcion = validated_data.get('descripcion'),
      categoria = validated_data.get('categoria'),
      dimensiones = validated_data.get('dimensiones'),
      referencia = validated_data.get('referencia'),
      foto = validated_data.get('foto'),
    )

  def update(self, instance, validated_data):
    # Una vez los datos han sido validados,
    # podemos actualizar una instancia del producto en base de datos
    #TODO --- Refactorizar con un bucle
    instance.nombre = validated_data.get('nombre', instance.nombre)
    instance.save()
    
    instance.precio = validated_data.get('precio', instance.descripcion)
    instance.save()
    
    instance.descripcion = validated_data.get('descripcion', instance.descripcion)
    instance.save()
    
    instance.categoria = validated_data.get('categoria', instance.categoria)
    instance.save()
    
    instance.dimensiones = validated_data.get('dimensiones', instance.dimensiones)
    instance.save()
    
    instance.referencia = validated_data.get('referencia', instance.referencia)
    instance.save()
    
    instance.foto = validated_data.get('foto', instance.foto)
    instance.save()

    return instance

  class Meta:
    model = Product
    fields = [ 
      'id', 
      'nombre', 
      'precio',
      'descripcion', 
      'categoria', 
      'dimensiones', 
      'referencia', 
      'foto' 
    ]
