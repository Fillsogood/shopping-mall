from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/orders/", include("orders.urls")),
    path("api/v1/address/", include("address.urls")),
    # path("api/v1/payments/", include("payments.urls")),
    path("api/v1/orderitems/", include("orderitems.urls")),
]
