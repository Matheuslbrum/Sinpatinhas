from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenRefreshView

from .services.auth import AuthService
from .services.profile import ProfileService
from .serializers import SavedSightingSerializer


# ===========================================
# REGISTER
# ===========================================
class RegisterView(APIView):
    def post(self, request):
        service = AuthService()
        result = service.register_user(request.data)

        if not result["success"]:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)


# ===========================================
# LOGIN
# ===========================================
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        service = AuthService()
        result = service.login_user(email, password)

        if not result["success"]:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


# ===========================================
# REFRESH TOKEN
# ===========================================
class RefreshTokenView(TokenRefreshView):
    pass


# ===========================================
# USER PROFILE (GET / UPDATE)
# ===========================================
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retorna dados do usuário logado.
        """
        service = ProfileService()
        data = service.get_profile(request.user)
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request):
        """
        Atualiza dados básicos do perfil: name, phone, username, etc.
        """
        service = ProfileService()
        result = service.update_profile(request.user, request.data)

        if not result["success"]:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


# ===========================================
# UPDATE AVATAR (UPLOAD)
# ===========================================
class UpdateAvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        """
        Atualiza somente o avatar do usuário.
        request.FILES["avatar"] deve existir.
        """
        if "avatar" not in request.FILES:
            return Response(
                {"success": False, "message": "Envie um arquivo 'avatar'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        avatar_file = request.FILES["avatar"]

        service = ProfileService()
        result = service.update_avatar(request.user, avatar_file)

        if not result["success"]:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        print(request)
        service = ProfileService()
        result = service.delete_user(request.user)

        if not result["success"]:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
    
class ToggleSaveSightingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, sighting_id):
        print(request.user)
        service = ProfileService()
        result = service.toggle(request.user, sighting_id)


        if not result["success"]:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class MySavedSightingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = ProfileService()
        saved = service.list_saved(request.user)
        serializer = SavedSightingSerializer(saved, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
