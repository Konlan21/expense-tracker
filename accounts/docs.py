from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import (
    SignupRequestSerializer,
    CustomTokenObtainPairSerializer,
    LogoutSerializer,
    UserProfileSerializer,
)

# -------------------------
# Signup
# -------------------------
signup_schema = dict(
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
            value={"id": "uuid", "email": "user@example.com", "message": "User created successfully"},
            response_only=True,
        ),
    ],
)

# -------------------------
# Login
# -------------------------
login_schema = dict(
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
                "id": "uuid",
                "email": "user@example.com",
                "message": "User logged in successfully",
            },
            response_only=True,
        ),
    ],
)

# -------------------------
# Logout
# -------------------------
logout_schema = dict(
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

# -------------------------
# User Profile – per endpoint
# -------------------------
user_profile_schemas = {
    "retrieve": dict(
        description="Retrieve a user's profile by ID",
        responses={200: UserProfileSerializer},
        examples=[
            OpenApiExample(
                "Get Profile Success Response",
                value={
                    "id": "uuid",
                    "email": "user@example.com",
                    "username": "newuser",
                    "first_name": "John",
                    "last_name": "Doe",
                },
                response_only=True,
            )
        ],
    ),
    "update": dict(
        description="Update a user's profile by ID",
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer},
        examples=[
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
            OpenApiExample(
                "Update Profile Response Example",
                value={
                    "id": "uuid",
                    "email": "user@example.com",
                    "username": "updateduser",
                    "first_name": "Updated",
                    "last_name": "User",
                },
                response_only=True,
            ),
        ],
    ),
    "partial_update": dict(
        description="Partially update a user's profile by ID",
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer},
        examples=[
            OpenApiExample(
                "Partial Update Profile Request Example",
                value={"first_name": "Updated"},
                request_only=True,
            ),
            OpenApiExample(
                "Partial Update Profile Response Example",
                value={
                    "id": "uuid",
                    "email": "user@example.com",
                    "username": "newuser",
                    "first_name": "Updated",
                    "last_name": "Doe",
                },
                response_only=True,
            ),
        ],
    ),
}
