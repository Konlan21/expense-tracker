
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from drf_spectacular.utils import extend_schema, OpenApiExample

from .serializers import (
    SignupRequestSerializer,
    CustomTokenObtainPairSerializer,
    LogoutSerializer,
    UserProfileSerializer,
)
from .models import User



# Signup user
@extend_schema(
    tags=["Accounts"],
    description="Register a new user with email, username, first_name, last_name and password.",
    request=SignupRequestSerializer,
    responses={201: {"example": {"id": "uuid", "email": "user@example.com", "message": "User created successfully"}}},
    examples=[
        OpenApiExample(
            "Signup Request Example",
            value={
                "email": "user@example.com",
                "username": "newuser",
                "first_name": "John",
                "last_name": "Doe",
                "password": "Password@123",
                "confirm_password": "Password@123",
            },
            request_only=True,
        ),
        OpenApiExample(
            "Signup Success Response",
            value={
                "id": "c9f2c7c0-1c8f-4c8f-9c3a-b63a5b62cafa",
                "email": "user@example.com",
                "message": "User created successfully",
            },
            response_only=True,
        ),
    ],
)


class SignupView(APIView):
    serializer_class = SignupRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"id": str(user.id), "email": user.email, "message": "User created successfully"},
            status=status.HTTP_201_CREATED,
        )



# Login user (JWT)
@extend_schema(
    tags=["Accounts"],
    description="Login user with email and password to receive JWT access and refresh tokens.",
    request=CustomTokenObtainPairSerializer,
    responses={200: CustomTokenObtainPairSerializer},
    examples=[
        OpenApiExample(
            "Login Request Example",
            value={"email": "user@example.com", "password": "Password@123"},
            request_only=True,
        ),
        OpenApiExample(
            "Login Success Response",
            value={
                "refresh": "string.jwt.token",
                "access": "string.jwt.token",
                "id": "c9f2c7c0-1c8f-4c8f-9c3a-b63a5b62cafa",
                "email": "user@example.com",
                "message": "User logged in successfully",
            },
            response_only=True,
        ),
    ],
)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]



# Logout user
@extend_schema(
    tags=["Accounts"],
    description="Logout user by blacklisting the refresh token.",
    request=LogoutSerializer,
    responses={200: {"example": {"message": "User logged out successfully"}}},
    examples=[
        OpenApiExample(
            "Logout Request Example",
            value={"refresh": "string.jwt.refresh.token"},
            request_only=True,
        ),
        OpenApiExample(
            "Logout Success Response",
            value={"message": "User logged out successfully"},
            response_only=True,
        ),
    ],
)
class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)


# User Profile schema defintion
@extend_schema(
    tags=["Accounts"],
    description="Retrieve or update a user's profile by ID.",
    responses={200: UserProfileSerializer},
    examples=[
        OpenApiExample(
            "Get Profile Success Response",
            value={
                "id": "c9f2c7c0-1c8f-4c8f-9c3a-b63a5b62cafa",
                "email": "user@example.com",
                "username": "newuser",
                "first_name": "John",
                "last_name": "Doe",
            },
            response_only=True,
        ),
        OpenApiExample(
            "Update Profile Request Example",
            value={
                "email": "user@example.com",
                "username": "updateduser",
                "first_name": "Updated",
                "last_name": "User",
            },
            request_only=True,
        ),
    ],
)


# User Profile

class UserProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except ValueError:
            return Response({"detail": "Invalid user ID"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValueError:
            return Response({"detail": "Invalid user ID"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
