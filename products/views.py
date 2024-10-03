from typing import Any

from django.shortcuts import get_object_or_404, render
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product
from .serializers import ProductDetailSerializer, ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    # 전체 제품 목록 조회
    @extend_schema(tags=["Product"])
    def list(self, request: Request) -> Response:
        products = self.queryset
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)


class ProductDetailViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # 제품 상세 조회
    @extend_schema(tags=["Product"])
    def retrieve(self, request: Request, pk: int) -> Response:
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data)

    # 제품 추가
    @extend_schema(tags=["Product"])
    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 제품 수정
    @extend_schema(tags=["Product"])
    def update(self, request: Request, pk: int) -> Response:
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 제품 삭제
    @extend_schema(tags=["Product"])
    def destroy(self, request: Request, pk: int) -> Response:
        product = get_object_or_404(self.queryset, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
