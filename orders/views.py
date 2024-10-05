from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import Http404
from .models import Order
from typing import Any
from .serializers import OrderSerializer, OrderDetailSerializer

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(tags=['Order'], responses={200: OrderSerializer(many=True)})
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # 주문 목록 조회
        orders = self.get_queryset()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(tags=['Order'], request=OrderDetailSerializer, responses={201: OrderDetailSerializer})
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # 주문 생성 요청 처리
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_object(self, pk: int):
        try:
            return self.get_queryset().get(pk=pk)
        except Order.DoesNotExist:
            raise Http404  # 주문이 존재하지 않을 경우 404 에러 발생

    @extend_schema(tags=['Order'], responses={200: OrderSerializer})
    def retrieve(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        # 개별 주문 조회
        order = self.get_object(pk)  # 주문 객체 가져오기
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=['Order'], request=OrderDetailSerializer, responses={200: OrderDetailSerializer})
    def update(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        # 주문 업데이트
        order = self.get_object(pk)  # 주문 객체 가져오기
        serializer = OrderDetailSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(tags=['Order'], responses={204: str, 404: str})
    def destroy(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        # 주문 삭제
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
