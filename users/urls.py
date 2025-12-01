from django.urls import path
from .views import (
    LoginView,
    RegisterView,
    RefreshTokenView,
    ProfileView,
    UpdateAvatarView,
    DeleteUserView,
    ToggleSaveSightingView,
    MySavedSightingsView,
)

urlpatterns = [
    # AUTH
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),

    # PROFILE
    path("me/", ProfileView.as_view(), name="profile"),
    path("avatar/", UpdateAvatarView.as_view(), name="avatar_update"),
    path("delete/", DeleteUserView.as_view(), name="delete_user"),
      
    path("<uuid:sighting_id>/save/", ToggleSaveSightingView.as_view(), name="save-sighting"),
    path("save/", MySavedSightingsView.as_view(), name="my-save-sightings"),

]
