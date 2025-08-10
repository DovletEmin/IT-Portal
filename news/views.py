from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import TextNews, VideoNews
from .serializers import TextNewsSerializer, VideoNewsSerializer


class TextNewsViewSet(viewsets.ModelViewSet):
    queryset = TextNews.objects.all()
    serializer_class = TextNewsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class VideoNewsViewSet(viewsets.ModelViewSet):
    queryset = VideoNews.objects.all()
    serializer_class = VideoNewsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']