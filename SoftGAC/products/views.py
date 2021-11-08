from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Product
from .serializers import ProductSerializer

from django.shortcuts import render

class ProductListView(
  APIView, # Clase basica de vista que provee Django Rest Framework
  UpdateModelMixin, # Mixin que permite a APIView manejar las solicitudes Http PUT
  DestroyModelMixin, # Mixin que permite manejar solicitudes DELETE
):

  def get(self, request, id=None):
    if id:
    # Si se pasa el id en la solicitud GET, se devuelve un item 
    # de productos identificado por tal id
      try:
        # quiere actualizar existe 
        # Revisa si el item de producto que el usuario 
        queryset = Product.objects.get(id=id)
        print(query)
      except Todo.DoesNotExist:
        # Si el item de no existe, retorna un mensaje de error
        return Response( {'errors' : ' This product item does not exist'}, status=400)

      # Serializamos el item de producto desde el queryset de Django y
      # transformamos los datos en formato JSON
      read_serializer = ProductSerializer(queryset)

    else:
      # Solicitamos todos los items de producto a 
      # la base de datos usand Django's model ORM
      queryset = Product.objects.all()

      read_serializer = ProductSerializer(
        queryset, many=True
      )
    
    return Response(read_serializer.data)
  
  def post(self, request):
    # Pasar datos JSON de la solicitud POST para validacion
    create_serializer = ProductSerializer(data=request.data)
    print(create_serializer)

    # Revisamos si los datos de la solisitud POST pasa la validacion hecho desde el serializer
    if create_serializer.is_valid():

      # Si los datos que envia el usuario son validos, 
      # se crea un nuevo producto en la base de datos
      product_item_object = create_serializer.save()

      # Serializamos(transformar) el nuevo item de producto 
      # de un objeto de Python a formato JSON
      read_serializer = ProductSerializer(product_item_object)

      ## Retornamos la respuesta HTTP con los datos del nuevo producto
      return Response(read_serializer.data, status=201)

    # Si los datos enviados no son validos, retornamos un codido 400 con un mensaje de errors
    return Response(create_serializer.errors, status=400)
  
  def put(self, request, id=None):
    try:
      # Revisamos si el item de producto que el usuario quiere actualizar existe
      product_item = Product.objects.get(id=id)
    except Product.DoesNotExist:
      return Response({'errors': 'This product item does not exist'}, status=400)
    

    update_serializer = ProductSerializer(product_item, data=request.data)
    # Si los datos a actualizar son validos, procedemos a guardar los datos en la base de datos
    if update_serializer.is_valid():
      
      # datos validos, actualizar el item de producto en la base de datos
      product_item_object = update_serializer.save()

      # Serializamos el item de producto de objeto Python a JSON
      read_serializer = ProductSerializer(product_item_object)

      return Response(read_serializer.data, status=200)
    
    # Si los datos no son validos, retornar una respuesta de error
    return Response(update_serializer.errors, status=400)
  
  def delete(self, request, id=None):
    try:
      # Revisamos si el item de producto que el usuario quiere eliminar existe
      product_item = Product.objects.get(id=id)
    except Product.DoesNotExist:
      # Si item de producto no existe, retornan un mensaje de error
      return Response({'errors': 'This product item does not exist.'}, status=400)
    
    # Eliminar el item de la base de datos
    product_item.delete()

    #retorna una respuesta HTTP notificando que el item fue eliminado exitosamente
    return Response(status=204)




