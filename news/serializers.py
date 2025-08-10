from rest_framework import serializers
from .models import TextNews, VideoNews

class TextNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNews
        fields = '__all__'


class VideoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNews
        fields = '__all__'