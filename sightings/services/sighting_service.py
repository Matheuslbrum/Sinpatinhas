from sightings.models import Sighting
from django.core.exceptions import PermissionDenied


class SightingService:

    @staticmethod
    def create_sighting(data, user):
        """
        Cria um registro de animal associado ao usuário autenticado.
        """
        sighting = Sighting.objects.create(
            user=user,
            **data
        )
        return sighting

    @staticmethod
    def list_sightings():
        """
        Retorna todos os animais registrados.
        """
        return Sighting.objects.all()

    @staticmethod
    def retrieve_sighting(sighting_id):
        return Sighting.objects.get(id=sighting_id)
    
    def list_user_sightings(user):
        return Sighting.objects.filter(user=user).order_by("-created_at")

    def delete_sighting(sighting_id, user):
        sighting = Sighting.objects.get(id=sighting_id)

        # garantia de segurança
        if sighting.user != user:
            raise PermissionDenied("Você não tem permissão para excluir este avistamento.")

        sighting.delete()
        return True
