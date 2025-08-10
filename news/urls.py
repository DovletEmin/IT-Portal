from rest_framework import routers
from django.urls import path, include
from .views import TextNewsViewSet, VideoNewsViewSet

router = routers.DefaultRouter()
router.register(r'text-news', TextNewsViewSet)
router.register(r'video-news', VideoNewsViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]