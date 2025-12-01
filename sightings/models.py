import uuid
from django.db import models


class Sighting(models.Model):
    TYPE_CHOICES = (
        ("LOST", "Lost"),
        ("FOUND", "Found"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    animal_name = models.CharField(max_length=100, blank=True, null=True)
    specie = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="sightings")

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    image_url = models.TextField(blank=True, null=True)

    ai_prediction_radius_km = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sighting {self.id} - {self.animal_name}"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comments")
    sighting = models.ForeignKey("sightings.Sighting", on_delete=models.CASCADE, related_name="comments")

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário por {self.user.email}"

