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
        serializer = SightingSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        sighting = SightingService.create_sighting(
            data=serializer.validated_data,
            user=request.user
        )

        return Response(SightingSerializer(sighting).data, status=201)


class SightingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, sighting_id):
        sighting = SightingService.retrieve_sighting(sighting_id)
        return Response(SightingSerializer(sighting).data)


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
