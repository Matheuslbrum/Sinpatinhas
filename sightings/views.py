import base64
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import SightingSerializer, CommentSerializer
from .services.sighting_service import SightingService
from .services.comment_service import CommentService


class SightingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sightings = SightingService.list_sightings()
        serializer = SightingSerializer(sightings, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Agora aceita multipart/form-data com campo 'image'.
        O serializer converte automaticamente para base64
        e salva em image_url.
        """
        serializer = SightingSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Já vem com image_url preenchido se teve imagem
        validated = serializer.validated_data

        sighting = SightingService.create_sighting(
            data=validated,
            user=request.user
        )

        return Response(SightingSerializer(sighting).data, status=status.HTTP_201_CREATED)

class SightingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, sighting_id):
        sighting = SightingService.retrieve_sighting(sighting_id)
        return Response(SightingSerializer(sighting).data)
    
    def delete(self, request, sighting_id):
        try:
            SightingService.delete_sighting(sighting_id, request.user)
            return Response({"message": "Avistamento deletado com sucesso."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, sighting_id):
        comments = CommentService.list_comments(sighting_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, sighting_id):
        serializer = CommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        comment = CommentService.create_comment(
            sighting_id=sighting_id,
            text=serializer.validated_data["text"],
            user=request.user
        )

        return Response(CommentSerializer(comment).data, status=201)
    
class PublicSightingListView(APIView):

    def get(self, request):
        sightings = SightingService.list_sightings()
        serializer = SightingSerializer(sightings, many=True)
        return Response(serializer.data)

class MySightingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sightings = SightingService.list_user_sightings(request.user)
        serializer = SightingSerializer(sightings, many=True)
        return Response(serializer.data)
