from django.db.models.query import QuerySet
from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from typing import Any
from .models import Address
from .serializers import AddressDetailSerializer, AddressSerializer


class AddressViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self) -> QuerySet[Address]:
        return Address.objects.all()
    
    @extend_schema(tags=["Address"], responses={200: AddressSerializer(many=True)})
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        addresses = self.get_queryset()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)
    
    @extend_schema(tags=["Address"],request=AddressSerializer, responses={200: AddressDetailSerializer})
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AddressDetailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self) -> QuerySet[Address]:
        return Address.objects.all()
    
    def get_object(self, pk: int) -> Address:
        try:
            return self.get_queryset().get(pk=pk)
        except Address.DoesNotExist:
            raise Http404
        
    @extend_schema(tags=["Address"], responses={200: AddressDetailSerializer})
    def retrieve(self, pk: int, request: Request, *args: Any, **kwargs: Any) -> Response:
        address = self.get_object(pk)
        serializer = AddressDetailSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(tags=["Address"],request=AddressSerializer, responses={200: AddressDetailSerializer})
    def update(self, pk: int, request: Request, *args: Any, **kwargs: Any) -> Response:
        address = self.get_object(pk)
        serializer = AddressDetailSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(tags=["Address"], responses={200: AddressDetailSerializer})
    def destroy(self, pk: int, request: Request, *args: Any, **kwargs: Any) -> Response:
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
