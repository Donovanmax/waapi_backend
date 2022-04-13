
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import serializers, status, filters

from .models import Business, Detail, Type, Comment, Account
from .serializers import BusinessSerializer, DetailSerializer,\
    AccountSerializer, TypeSerializer, AccountGmailSerializer





class TypesView(APIView):
    def get(self, request,  format=None):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        if request.method == "POST":
             serializer = TypeSerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()     
                 return Response(serializer.data, status=status.HTTP_201_CREATED)   
             else:         
                 return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    



class AccountViews(APIView):
       
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request, format=None, *args, **kwargs):
        user = Account.objects.all()
        serializer = AccountSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request):
        ko = { 'etat':  'no'} 
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()     
            return Response(serializer.data, status=status.HTTP_201_CREATED)            
        else:         
            print("error", serializer.errors)
            return Response(data=(ko) )   
        

class AccountGmailViews(APIView):
    def get(self, request, format=None,):
        user = Account.objects.all()
        serializer = AccountGmailSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountGmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()     
            return Response(serializer.data, status=status.HTTP_201_CREATED)            
        else:         
            print("error", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                
                 
class AccountLoginViews(APIView):
    
    def get(self, request, query, format=None):
        ok = { 'etat':  'yes'}
        ko = { 'etat':  'no'}
        user = Account.objects.filter(username=query)
        serializer = AccountSerializer(user, many=True)
        if user.exists():
            
            return Response(data = (ok, serializer.data))
        
        else:
            return Response(ko)
        
           
    
class BusinessList(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request,  format=None):
        business = Business.objects.all()
        serializer = BusinessSerializer(business, many=True, context={'request': request})
        return Response(serializer.data)

class DetailsList(APIView):
    def get(self, request, id, format=None, ):
        detail = Detail.objects.filter(business_id___id= id) 
        serializer = DetailSerializer(detail, many=True, context={'request': request})
        return Response(serializer.data)
    
class BusinessDetails(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request,  id, format=None):
        business = Business.objects.filter(_id = id)
        serializer = BusinessSerializer(business, many=True, context={'request': request})
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request, query , format=None, ):
        business = Business.objects.filter(type_id__types__startswith = query)
        serializer = BusinessSerializer(business, many=True, context={'request': request})
        return Response(serializer.data)
        
class RestoMenu(APIView):
    def get(self, request, id, format=None, ):
        business = Business.objects.filter(type_id__types = 'restaurants')
    
        #serializer = RestoWithMenuSerializer(restos, many=True, context={'request': request})
        return Response(business) #serializer.data,)

