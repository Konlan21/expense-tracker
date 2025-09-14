from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .serializers import (
    SignupRequestSerializer,
    CustomTokenObtainPairSerializer,
    LogoutSerializer,
    UserProfileSerializer,
    SignupResponseSerializer
)
from .models import User
from .docs import signup_schema, login_schema, logout_schema, profile_schema



# Signup
@signup_schema
class SignupView(APIView):
    serializer_class = SignupRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_serializer = SignupResponseSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


@login_schema
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]


#Logout 
@logout_schema
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


# User Profile
@profile_schema
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
