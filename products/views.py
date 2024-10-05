from typing import Any

from django.shortcuts import get_object_or_404
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
    permission_classes = [AllowAny]

    # 전체 제품 목록 조회
    @extend_schema(tags=["Product"], responses={200: ProductSerializer(many=True)})
    def list(self, request: Request) -> Response:
        products = self.queryset
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # 제품 추가
    @extend_schema(tags=["Product"], request=ProductSerializer, responses={201: ProductSerializer, 400: str})
    def create(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # 제품 상세 조회
    @extend_schema(tags=["Product"], responses={200: ProductDetailSerializer, 404: str})
    def retrieve(self, request: Request, pk: int) -> Response:
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    # 제품 수정
    @extend_schema(tags=["Product"], request=ProductDetailSerializer, responses={200: ProductDetailSerializer, 400: str, 404: str})
    def update(self, request: Request, pk: int) -> Response:
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductDetailSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 제품 삭제
    @extend_schema(tags=["Product"], responses={204: str, 404: str})
    def destroy(self, request: Request, pk: int) -> Response:
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
