from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Voice, Image, Video

from os import getenv


class VoiceSerializer(ModelSerializer):
    voice_file = SerializerMethodField()

    def get_voice_file(self, obj):
        voice_url = f'{getenv("GATEWAY_SCHEME")}://{getenv("EXTERNAL_IP_ADDRESS")}:{getenv("GATEWAY_PORT")}/media/{obj.voice_file}'
        return voice_url
    class Meta:
        model = Voice
        fields = "__all__"


class ImageSerializer(ModelSerializer):
    image_file = SerializerMethodField()

    def get_image_file(self, obj):
        img_url = f'{getenv("GATEWAY_SCHEME")}://{getenv("EXTERNAL_IP_ADDRESS")}:{getenv("GATEWAY_PORT")}/media/{obj.image_file}'
        return img_url

    class Meta:
        model = Image
        fields = "__all__"


class VideoSerializer(ModelSerializer):
    video_file = SerializerMethodField()

    def get_video_file(self, obj):
        video_url = f'{getenv("GATEWAY_SCHEME")}://{getenv("EXTERNAL_IP_ADDRESS")}:{getenv("GATEWAY_PORT")}/media/{obj.video_file}'
        return video_url
    class Meta:
        model = Video
        fields = "__all__"
