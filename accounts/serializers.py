# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
import re


# Signup Serialzier
class SignupRequestSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    # Field-level validation for email
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    # Field-level validation for username
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    # Object-lev validation for password
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password', None)

        errors = {}

        # Django built-in validators
        try:
            validate_password(password, user=self.instance)
        except serializers.ValidationError as e:
            errors['password'] = list(e.messages)

        # Confirm password
        if confirm_password != password:
            errors['confirm_password'] = ["Passwords do not match"]

        # Custom Validators
        pattern_checks = [
            (r'.*[A-Z].*', "Password must contain at least 1 uppercase letter."),
            (r'.*[a-z].*', "Password must contain at least 1 lowercase letter."),
            (r'.*\d.*', "Password must contain at least 1 number."),
            (r'.*[\W_].*', "Password must contain at least 1 special character."),
        ]

        for pattern, message in pattern_checks:
            if not re.search(pattern, password):
                errors.setdefault('password', []).append(message)

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SignupResponseSerializer(serializers.ModelSerializer):
    message = serializers.CharField(default="User created successfully")

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'message')



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


# Login serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except AuthenticationFailed:

            # Return 400 for invalid credentials  
            raise serializers.ValidationError({"detail": "Invalid email or password"})

        # Add extra user info
        data.update({
            "id": str(self.user.id),
            "email": self.user.email,
            "message": "User logged in successfully"
        })
        return data




# Logout Serializer
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        required=True,
        help_text="Refresh token to be blacklisted on logout",
    )