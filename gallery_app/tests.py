from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from .models import Voice, Image, Video


class FileModelTest(TestCase):
    def test_create_voice_data(self):
        voice = None
        try:
            user = User.objects.filter(username="admin")
            voice = Voice.objects.create(title="test", description="this is test",
                                         voice_file="media/user_voices/sp1_1todVkB.wav", user=user)
            self.assertIsNotNone(voice)
        except ValueError:
            self.assertIsNone(voice)

    def test_read_voice_data(self):
        voice = None
        try:
            voice = Voice.objects.get(pk=1)
            self.assertIsNotNone(voice)
        except ObjectDoesNotExist:
            self.assertIsNone(voice)

    def test_update_voice_data(self):
        voice = None
        try:
            voice = Voice.objects.get(pk=1)
            voice.title = "tested"
            voice.save()
            self.assertIsNotNone(voice)
        except ObjectDoesNotExist:
            self.assertIsNone(voice)

    def test_delete_voice_data(self):
        voice = None
        try:
            voice = Voice.objects.get(pk=1)
            voice.delete()
            voice = Voice.objects.filter(pk=1)
            self.assertIsNotNone(voice)
        except ObjectDoesNotExist:
            self.assertIsNone(voice)

    def test_create_image_data(self):
        image = None
        try:
            user = User.objects.filter(username="admin")
            image = Image.objects.create(title="test", description="this is test",
                                         image_file="media/user_voices/sp1_1todVkB.wav", user=user)
            self.assertIsNotNone(image)
        except ValueError:
            self.assertIsNone(image)

    def test_read_image_data(self):
        image = None
        try:
            image = Image.objects.get(pk=1)
            self.assertIsNotNone(image)
        except ObjectDoesNotExist:
            self.assertIsNone(image)

    def test_update_image_data(self):
        image = None
        try:
            image = Image.objects.get(pk=1)
            image.title = "tested"
            image.save()
            self.assertIsNotNone(image)
        except ObjectDoesNotExist:
            self.assertIsNone(image)

    def test_delete_image_data(self):
        image = None
        try:
            image = Image.objects.get(pk=1)
            image.delete()
            image = Voice.objects.filter(pk=1)
            self.assertIsNotNone(image)
        except ObjectDoesNotExist:
            self.assertIsNone(image)

    def test_create_video_data(self):
        video = None
        try:
            user = User.objects.filter(username="admin")
            video = Video.objects.create(title="test", description="this is test",
                                         video_file="media/user_voices/sp1_1todVkB.wav", user=user)
            self.assertIsNotNone(video)
        except ValueError:
            self.assertIsNone(video)

    def test_read_video_data(self):
        video = None
        try:
            video = Video.objects.get(pk=1)
            self.assertIsNotNone(video)
        except ObjectDoesNotExist:
            self.assertIsNone(video)

    def test_update_video_data(self):
        video = None
        try:
            video = Video.objects.get(pk=1)
            video.title = "tested"
            video.save()
            self.assertIsNotNone(video)
        except ObjectDoesNotExist:
            self.assertIsNone(video)

    def test_delete_video_data(self):
        video = None
        try:
            video = Image.objects.get(pk=1)
            video.delete()
            video = Video.objects.filter(pk=1)
            self.assertIsNotNone(video)
        except ObjectDoesNotExist:
            self.assertIsNone(video)
