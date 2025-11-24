import uuid
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class AuthService:

    # ===========================================
    # REGISTER USER
    # ===========================================
    def register_user(self, data):
        required_fields = ["email", "name", "password", "phone"]
        print(data)
        for field in required_fields:
            if field not in data or not data[field]:
                return {"success": False, "message": f"Campo obrigatório: {field}"}

        if User.objects.filter(email=data["email"]).exists():
            return {"success": False, "message": "Email já cadastrado."}

        user = User.objects.create(
            id=uuid.uuid4(),
            email=data["email"],
            username=data["name"],
            phone_number=data["phone"],
            password=make_password(data["password"])
        )

        # 🔥 GERA TOKEN AUTOMÁTICO APÓS REGISTRO
        refresh = RefreshToken.for_user(user)

        return {
            "success": True,
            "message": "Usuário registrado com sucesso.",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": str(user.id),
                "email": user.email,
                "username": user.username,
                "phone": user.phone_number,
                "avatar": None,
            },
        }

    # ===========================================
    # LOGIN
    # ===========================================
    def login_user(self, email, password):
        user = authenticate(email=email, password=password)

        if not user:
            return {"success": False, "message": "Credenciais inválidas."}

        refresh = RefreshToken.for_user(user)

        return {
            "success": True,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": str(user.id),
                "email": user.email,
                "username": user.username,
                "phone": user.phone_number,
                "avatar": user.avatar_url.url if user.avatar_url else None,
            },
        }
