from datetime import datetime, timedelta
from typing import Any, cast

from django.contrib.auth import authenticate
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserDetailSerializer, UserSignupSerializer


class SignupViewSet(viewsets.ViewSet):
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    # 회원가입
    @extend_schema(tags=["User"])
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully!", "user": UserSignupSerializer(user).data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTLoginView(TokenObtainPairView):
    @extend_schema(tags=["User"])
    # 로그인 시 토큰 발급
    def post(self, request: Request) -> Response:
        try:
            user = authenticate(
                request=request, user_id=request.data.get("user_id"), password=request.data.get("password")
            )
            if user is not None:
                user.last_login = timezone.now()
                user.save()
                response = super().post(request)
                refresh_token = response.data.get("refresh")
                del response.data["refresh"]
                response.set_cookie(
                    "AUT_REF",
                    refresh_token,
                    samesite=None,
                    secure=False,
                    httponly=False,
                    expires=datetime.now() + timedelta(days=1),
                )
                return response
            else:
                return Response(
                    {"msg": "유저 아이디 또는 비밀번호가 올바르지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class JWTLogoutView(viewsets.ViewSet):
    # 로그아웃
    @extend_schema(tags=["User"])
    def post(self, request: Request) -> Response:
        response = Response({"msg": "로그아웃 성공"}, status=status.HTTP_200_OK)
        response.delete_cookie("AUT_REF")  # 쿠키에서 리프레시 토큰 삭제
        return response


class JWTRefreshView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []

    # 토큰 재발급
    @extend_schema(tags=["User"])
    def post(self, request: Request) -> Response:
        refresh_token = request.COOKIES.get("AUT_REF")
        if refresh_token:
            try:
                token = RefreshToken(cast(Token, refresh_token))
                new_access_token = str(token.access_token)
                response = Response({"access": new_access_token}, status=status.HTTP_200_OK)
                response.set_cookie(
                    "AUT_REF",
                    str(token),
                    samesite=None,
                    secure=False,
                    httponly=False,
                    expires=datetime.now() + timedelta(days=1),
                )
                return response
            except TokenError as e:
                return Response({"msg": f"리프레시 토큰 에러: {str(e)}"}, status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response(
                    {"msg": f"토큰 갱신 중 오류가 발생했습니다: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response({"msg": "토큰이 존재하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # 회원정보 조회
    @extend_schema(tags=["User"])
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = cast(User, request.user)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    # 회원정보 수정
    @extend_schema(tags=["User"])
    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = cast(User, request.user)
        serializer = UserDetailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원탈퇴
    @extend_schema(tags=["User"])
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = cast(User, request.user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
