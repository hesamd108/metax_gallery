from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CRUDVoiceViewSet, CRUDImageViewSet, CRUDVideoViewSet

router = DefaultRouter()

router.register('voice', CRUDVoiceViewSet)
router.register('image', CRUDImageViewSet)
router.register('video', CRUDVideoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
