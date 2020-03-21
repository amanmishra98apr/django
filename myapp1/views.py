from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IndianIndices,IndianIndices2,GlobalIndices,GlobalIndices2,BSE,BSE2,NSE,NSE2,Sensex,Nifty,FillAndDill_Cash,FillAndDill_SEBI,FillAndDill_Cash2,Fill_SEBI2
from .serializers import IndianIndicesSerializer,IndianIndices2Serializer,GlobalIndicesSerializer,GlobalIndices2Serializer,BSESerializer,BSE2Serializer,NSESerializer,NSE2Serializer,SensexSerializer,NiftySerializer,FillAndDill_CashSerializer,FillAndDill_SEBISerializer,FillAndDill_Cash2Serializer,Fill_SEBI2Serializer
# Create your views here.
@api_view(['GET'])
def IndianIndices_list(request):
    if request.method=="GET":
        obj=IndianIndices.objects.all()
        serializer=IndianIndicesSerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def IndianIndices_list2(request):
    if request.method=="GET":
        obj=IndianIndices2.objects.all()
        serializer=IndianIndices2Serializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def GlobalIndices_list(request):
    if request.method=="GET":
        obj=GlobalIndices.objects.all()
        serializer=GlobalIndicesSerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def GlobalIndices2_list(request):
    if request.method=="GET":
        obj=GlobalIndices2.objects.all()
        serializer=GlobalIndices2Serializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def BSE_list(request):
    if request.method=="GET":
        obj=BSE.objects.all()
        serializer=BSESerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def BSE2_list(request):
    if request.method=="GET":
        obj=BSE2.objects.all()
        serializer=BSE2Serializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def NSE_list(request):
    if request.method=="GET":
        obj=NSE.objects.all()
        serializer=NSESerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def NSE2_list(request):
    if request.method=="GET":
        obj=NSE2.objects.all()
        serializer=NSE2Serializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def Sensex_list(request):
    if request.method=="GET":
        obj=Sensex.objects.all()
        serializer=SensexSerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def Nifty_list(request):
    if request.method=="GET":
        obj=Nifty.objects.all()
        serializer=NiftySerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def FillAndDill_Cash_list(request):
    if request.method=="GET":
        obj=FillAndDill_Cash.objects.all()
        serializer=FillAndDill_CashSerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def FillAndDill_SEBI_list(request):
    if request.method=="GET":
        obj=FillAndDill_SEBI.objects.all()
        serializer=FillAndDill_SEBISerializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def FillAndDill_Cash2_list(request):
    if request.method=="GET":
        obj=FillAndDill_Cash2.objects.all()
        serializer=FillAndDill_Cash2Serializer(obj,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def Fill_SEBI2_list(request):
    if request.method=="GET":
        obj=Fill_SEBI2.objects.all()
        serializer=Fill_SEBI2Serializer(obj,many=True)
        return Response(serializer.data)
