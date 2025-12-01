from django.core.files.uploadedfile import InMemoryUploadedFile
from users.models import User
from sightings.models import Sighting


class ProfileService:

    # ===========================================
    # GET USER PROFILE
    # ===========================================
    def get_profile(self, user: User):
        return {
            "id": str(user.id),
            "email": user.email,
            "username": user.username,
            "phone": user.phone_number,
            "avatar": user.avatar_url.url if user.avatar_url else None,
        }

    # ===========================================
    # UPDATE AVATAR
    # ===========================================
    def update_avatar(self, user: User, avatar_file: InMemoryUploadedFile):
        if not avatar_file:
            return {"success": False, "message": "Nenhum arquivo enviado."}

        user.avatar_url = avatar_file
        user.save()

        return {
            "success": True,
            "avatar": user.avatar_url.url,
            "message": "Avatar atualizado com sucesso.",
        }

    # ===========================================
    # DELETE USER
    # ===========================================
    def delete_user(self, user: User):
        try:
            user.delete()
            return {"success": True, "message": "Conta excluída com sucesso."}
        except Exception as e:
            return {"success": False, "message": f"Erro ao excluir conta: {str(e)}"}
        
    def toggle(self, user, sighting_id):
        try:
            sighting = Sighting.objects.get(id=sighting_id)
        except Sighting.DoesNotExist:
            return {"success": False, "message": "Sighting não encontrado."}

        result = user.toggle_save_sighting(sighting)

        return {
            "success": True,
            "saved": result["saved"],
            "message": result["message"]
        }

    @staticmethod
    def list_saved(user):
        return user.saved_sightings.all()
