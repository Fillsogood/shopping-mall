from django.urls import path

from . import views

urlpatterns = [
    # 제품 리스트
    path("", views.ProductViewSet.as_view({"get": "list", "post": "create"}), name="product_list_create"),
    # 개별 제품 조회, 수정, 삭제, 생성
    path(
        "<int:pk>/",
        views.ProductDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="product_detail_update_delete",
    ),
]
