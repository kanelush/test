
from ninja import NinjaAPI
from core.models import Category, Negocios
from typing import List
from core.schema import NegocioSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/negocios", response=List[NegocioSchema])
def negocios(request):
    return Negocios.objects.all()

@api.get("/negocios/{negocio_id}", response={200: NegocioSchema, 404:NotFoundSchema})
def negocio(request, negocio_id: int):
    try:
        negocio = Negocios.objects.get(pk=negocio_id)
        return 200, negocio
    except Negocios.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}

@api.post("/negocios", response={201: NegocioSchema})
def create_negocio(request, negocio: NegocioSchema):
    negocio = Negocios.objects.create(**negocio.dict())
    return negocio

@api.put("/negocios/{negocio_id}", response={200: NegocioSchema, 404:NotFoundSchema})
def change_negocio(request, negocio_id: int, data: NegocioSchema):
    try:
        negocio = Negocios.objects.get(pk=negocio_id)
        for attribute, value in data.dict().items():
             setattr(negocio, attribute, value)
        negocio.save()
        return 200, negocio
    except Negocios.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}
         
@api.delete("/negocios/{negocio_id}", response={200:None, 404:NotFoundSchema})
def delete_negocio(request, negocio_id: int, data: NegocioSchema):
    try:
        negocio = Negocios.objects.get(pk=negocio_id)
        negocio.delete()
        return 200 
    except Negocios.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}