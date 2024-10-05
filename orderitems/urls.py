from django.urls import path

from . import views

urlpatterns = [
    # Orderitem 리스트와 생성
    path("", views.OrderItemViewSet.as_view({"get": "list", "post": "create"}), name="order-list-create"),
    # 개별 Orderitem 조회, 수정, 삭제, 생성
    path(
        "<int:pk>/",
        views.OrderItemDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="order-detail-update-delete",
    ),
]
