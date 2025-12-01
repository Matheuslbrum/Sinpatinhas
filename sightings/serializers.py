from rest_framework import serializers
from .models import Sighting, Comment
import base64

class SightingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Sighting
        fields = "__all__"
        read_only_fields = ["id", "user", "image_url"]

    def validate(self, attrs):
        image_file = attrs.pop("image", None)

        if image_file:
            # Converte imagem para base64
            encoded = base64.b64encode(image_file.read()).decode("utf-8")

            attrs["image_url"] = f"data:{image_file.content_type};base64,{encoded}"

        return attrs


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Comment
        fields = "__all__"
