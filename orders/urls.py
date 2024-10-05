from django.urls import path

from . import views

urlpatterns = [
    # Order 리스트와 생성
    path("", views.OrderViewSet.as_view({"get": "list", "post": "create"}), name="order-list-create"),
    # 개별 Order 조회, 수정, 삭제, 생성
    path(
        "<int:pk>/",
        views.OrderDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="order-detail-update-delete",
    ),
]
