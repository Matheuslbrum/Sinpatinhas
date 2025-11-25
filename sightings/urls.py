from django.urls import path
from .views import (
    SightingListCreateView,
    SightingDetailView,
    CommentListCreateView,
    PublicSightingListView
)

urlpatterns = [
    path("", SightingListCreateView.as_view(), name="sighting-list-create"),
    path("<uuid:sighting_id>/", SightingDetailView.as_view(), name="sighting-detail"),
    path("<uuid:sighting_id>/comments/", CommentListCreateView.as_view(), name="comments"),
    path("sightings/all/", PublicSightingListView.as_view(), name="public-sightings"),
]
