from sightings.models import Sighting


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
