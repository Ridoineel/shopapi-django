from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from boutique.serializers import OrderDetailSerializer
import re

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("id", "username", "first_name", "last_name", "email", "password", "is_active")

class UserDetailSerializer(serializers.ModelSerializer):
	orders = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = ("id", "username", "first_name", "last_name", "email", "password", "is_active")

	def get_orders(self, instance):
		queryset = instance.orders

		serializer = OrderDetailSerializer(queryset, many=True)

		return serializer.data
		

class UserSigninSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("email", "password")

class UserWriteSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(
		validators=[UniqueValidator(
						queryset=User.objects.all(),
						message = "Cette adresse e-mail est déjà utilisée.")
					]
	)
	password = serializers.CharField(
		write_only=True, 
		validators=[validate_password]
	)

	class Meta:
		model = User
		fields = ["id", "username", "first_name", "last_name", "email", "password", "is_active", "is_superuser", "is_staff"]
		
		extra_kwargs = {
			"id": {"read_only": True},
			"is_active": {"read_only": True},
			"is_superuser": {"read_only": True},
			"is_staff": {"read_only": True},
        }
	

	def validate_first_name(self, value):
		if re.match(r"^[a-zA-zA-Z]+", value) is None:
			raise serializers.ValidationError("le prénom est invalide")
		
		return value
	
	def validate_last_name(self, value):
		if re.match(r"^[a-zA-Z][a-zA-Z -']+", value) is None:
			raise serializers.ValidationError("le nom est invalide")
		
		return value
		
class UserSignupSerializer(UserWriteSerializer):
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta(UserWriteSerializer.Meta):
		fields = ["id", "username", "first_name", "last_name", "email", "password", "password2", "is_active", "is_superuser", "is_staff"]

		extra_kwargs = {
			"id": {"read_only": True},
			"is_active": {"read_only": True},
			"is_superuser": {"read_only": True},
			"is_staff": {"read_only": True},
			"username": {"required": True},
            'first_name': {'required': True},
            'last_name': {'required': True},
			"email": {"required": True},
			"password": {"required": True},
			"password2": {"required": True}
        }

	
	def validate(self, data):
		if data["password"] != data["password2"]:
			raise serializers.ValidationError("Les deux mot de passe ne correspondent pas")

		return data
	
	def create(self, validated_data):
		validated_data.pop("password2")
		
		user = User.objects.create(**validated_data)

		user.set_password(validated_data.get("password"))
		user.save()

		return user


class UserUpdateSerializer(UserWriteSerializer):
	def validate_email(self, value):
		if self.email != value and User.objects.filter(email__iexact=value).exists():
			raise serializers.ValidationError("Cet email appartient déjà à un compte")

	
		return value
