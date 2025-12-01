from django.urls import path
from .views import (
    SightingListCreateView,
    SightingDetailView,
    CommentListCreateView,
    PublicSightingListView,
    MySightingsView,
)

urlpatterns = [
    path("", SightingListCreateView.as_view(), name="sighting-list-create"),
    path("<uuid:sighting_id>/", SightingDetailView.as_view(), name="sighting-detail"),
    path("<uuid:sighting_id>/comments/", CommentListCreateView.as_view(), name="comments"),
    path("all/", PublicSightingListView.as_view(), name="public-sightings"),
    path("my/", MySightingsView.as_view(), name="my-sightings"),
    path("sightings/<int:sighting_id>/", SightingDetailView.as_view()),
]
