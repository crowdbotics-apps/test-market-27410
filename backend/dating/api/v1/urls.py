from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    InboxViewSet,
    SettingViewSet,
    DislikeViewSet,
    LikeViewSet,
    UserPhotoViewSet,
    MatchViewSet,
    ProfileViewSet,
)

router = DefaultRouter()
router.register("profile", ProfileViewSet)
router.register("inbox", InboxViewSet)
router.register("dislike", DislikeViewSet)
router.register("setting", SettingViewSet)
router.register("userphoto", UserPhotoViewSet)
router.register("match", MatchViewSet)
router.register("like", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
