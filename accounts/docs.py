# accounts/docs.py
from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import (
    SignupRequestSerializer,
    CustomTokenObtainPairSerializer,
    LogoutSerializer,
    UserProfileSerializer,
)

# Signup schema
signup_schema = extend_schema(
    tags=["User"],
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

# Login schema
login_schema = extend_schema(
    tags=["User"],
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

# Logout schema
logout_schema = extend_schema(
    tags=["User"],
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

# User Profile schema
# accounts/docs.py
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample
from .serializers import UserProfileSerializer


profile_schema = extend_schema_view(
    get=extend_schema(
        tags=["User"],
        description="Retrieve a user's profile by ID.",
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
            )
        ],
    ),
    put=extend_schema(
        tags=["User"],
        description="Fully update a user's profile by ID.",
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer},
        examples=[
            OpenApiExample(
                "Update Profile Request Example (PUT)",
                value={
                    "email": "user@example.com",
                    "username": "updateduser",
                    "first_name": "Updated",
                    "last_name": "User",
                },
                request_only=True,
            )
        ],
    ),
    patch=extend_schema(
        tags=["User"],
        description="Partially update a user's profile by ID.",
        request=UserProfileSerializer,
        responses={200: UserProfileSerializer},
        examples=[
            OpenApiExample(
                "Partial Update Profile Request Example (PATCH)",
                value={
                    "first_name": "Updated",
                },
                request_only=True,
            )
        ],
    ),
)

