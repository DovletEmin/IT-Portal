from rest_framework import serializers
from .models import TextNews, VideoNews

class TextNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNews
        fields = ['title', 'category', 'description', "image"]

    def get_fields(self):
        fields = super().get_fields()
        if self.context.get('request') and self.context['request'].method == 'PATCH':
            for field in fields.values():
                field.required = False
        return fields


class VideoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNews
        fields = ['title', 'category', "video"]

    def get_fields(self):
        fields = super().get_fields()
        if self.context.get('request') and self.context['request'].method == 'PATCH':
            for field in fields.values():
                field.required = False
        return fields