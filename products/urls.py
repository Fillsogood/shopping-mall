from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductViewSet.as_view({"get": "list"}), name="product_list"),
    path("<int:pk>/", views.ProductDetailViewSet.as_view({"get": "retrieve"}), name="product_detail"),
    path("create/", views.ProductDetailViewSet.as_view({"post": "create"}), name="product_create"),
    path("<int:pk>/update/", views.ProductDetailViewSet.as_view({"put": "update"}), name="product_update"),
    path("<int:pk>/delete/", views.ProductDetailViewSet.as_view({"delete": "destroy"}), name="product_delete"),
]

