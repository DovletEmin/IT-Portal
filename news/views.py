from rest_framework import viewsets
from .models import TextNews, VideoNews
from .serializers import TextNewsSerializer, VideoNewsSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination


class TextNewsPagination(PageNumberPagination):
    page_size = 10

class VideoNewsPagination(PageNumberPagination):
    page_size = 10



class TextNewsViewSet(viewsets.ModelViewSet):
    queryset = TextNews.objects.all()
    serializer_class = TextNewsSerializer
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = TextNewsPagination
    http_method_names = ['get', 'post', 'patch', 'delete']

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)



class VideoNewsViewSet(viewsets.ModelViewSet):
    queryset = VideoNews.objects.all()
    serializer_class = VideoNewsSerializer
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = VideoNewsPagination
    http_method_names = ['get', 'post', 'patch', 'delete']

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)