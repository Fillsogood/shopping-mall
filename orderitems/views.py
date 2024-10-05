from django.db.models.query import QuerySet
from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from typing import Any
from .models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self) -> QuerySet[OrderItem]:
        return OrderItem.objects.all()  # type: ignore

    @extend_schema(tags=["OrderItem"], responses={200: OrderItemSerializer(many=True)})
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        order_items = self.get_queryset()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["OrderItem"], request=OrderItemSerializer, responses={201: OrderItemSerializer, 400: str})
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self) -> QuerySet[OrderItem]:
        return OrderItem.objects.all()  # type: ignore

    def get_object(self, pk: int) -> OrderItem:
        try:
            return self.get_queryset().get(pk=pk)
        except OrderItem.DoesNotExist:
            raise Http404

    @extend_schema(tags=["OrderItem"], responses={200: OrderItemSerializer})
    def retrieve(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        order_item = self.get_object(pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    @extend_schema(tags=["OrderItem"], request=OrderItemSerializer, responses={200: OrderItemSerializer, 400: str})
    def update(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        order_item = self.get_object(pk)
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(tags=["OrderItem"], responses={204: None, 404: str})
    def destroy(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        order_item = self.get_object(pk)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
