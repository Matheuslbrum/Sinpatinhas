from django.db import models
import uuid

class AIAnalysis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sighting = models.OneToOneField("sightings.Sighting", on_delete=models.CASCADE, related_name="analysis")

    species_predicted = models.CharField(max_length=100, blank=True, null=True)
    breed_predicted = models.CharField(max_length=100, blank=True, null=True)
    distance_radius_predicted = models.FloatField(blank=True, null=True)

    full_response_json = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Analysis for {self.sighting.id}"
