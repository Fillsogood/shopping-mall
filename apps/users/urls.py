from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from . import views

urlpatterns = [
    path("signup/", views.SignupViewSet.as_view({"post": "create"}), name="signup"),
    path("login/", views.JWTLoginView.as_view(), name="login"),
    path("logout/", views.JWTLogoutView.as_view({"post": "post"}), name="logout"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", views.JWTRefreshView.as_view({"post": "post"}), name="token_refresh"),
    path("info/", views.UserDetailViewSet.as_view({"get": "retrieve"}), name="user_info"),
    path("info/update/", views.UserDetailViewSet.as_view({"put": "update"}), name="user_update"),
    path("info/delete/", views.UserDetailViewSet.as_view({"delete": "destroy"}), name="user_delete"),
]
