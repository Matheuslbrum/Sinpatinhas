from django.urls import path
from .views import (
    LoginView,
    RegisterView,
    RefreshTokenView,
    ProfileView,
    UpdateAvatarView,
    DeleteUserView
)

urlpatterns = [
    # AUTH
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),

    # PROFILE
    path("me/", ProfileView.as_view(), name="profile"),
    path("avatar/", UpdateAvatarView.as_view(), name="avatar_update"),
    path("delete/", DeleteUserView.as_view(), name="delete_user"),  # 👈 nova rota
]
