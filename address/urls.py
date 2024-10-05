from django.urls import path
from .views import AddressDetailViewSet, AddressViewSet

urlpatterns = [
    path("", AddressViewSet.as_view({"get": "list","post": "create"}), name="address-list-create"),
    path("<int:pk>/", AddressDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="order-detail-update-delete",
    ),
]