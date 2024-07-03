from os import rename, getenv
from random import choice

from django import db, contrib, core
from rest_framework import response, viewsets

from . import models, serializers


class CRUDVoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Voice.objects.all().order_by('publish_date')
    serializer_class = serializers.VoiceSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = self.queryset
        # user = User.objects.get(username=self.request.user.username)
        user = models.User.objects.get(username='admin')
        query_set = queryset.filter(user=user)
        return query_set

    def list(self, request, *args, **kwargs):
        try:
            voices = models.Voice.objects.all()
            voice_serializer = serializers.VoiceSerializer(voices, many=True)
            return response.Response(voice_serializer.data, status=200)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def create(self, request, *args, **kwargs):
        try:
            # user = User.objects.get(username=request.user.username)
            user = contrib.auth.models.User.objects.get(username=getenv('DJANGO_SUPERUSER_USERNAME'))
            voice = models.Voice.objects.create(voice_file=request.data['voice_file'],
                                                user=user)
            voice.save()
            voice.file_name = str(voice.voice_file).split('/')[-1]
            voice.save()
            message = "the voice created"
            explanation = "the voice has been created successfully"

            return response.Response({"message": message, "explanation": explanation}, status=201)

        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def update(self, request, *args, **kwargs):
        if len(request.data['file_name'].split('.')) != 2:
            message = "invalid file name"
            explanation = "the file name should not have extra point"

            return response.Response({"message": message, "explanation": explanation}, status=200)
        try:
            voice = models.Voice.objects.get(pk=self.kwargs['pk'])
            old_file_path = voice.voice_file.path
            voice.file_name = request.data['file_name']
            voice.voice_file = f"voices/{request.data['file_name']}"
            voice.save()
            rename(old_file_path, f"media/voices/{request.data['file_name']}")
            message = "the voice updated"
            explanation = "the voice has been updated successfully"

            return response.Response({"message": message, "explanation": explanation}, status=200)
        except core.exceptions.ObjectDoesNotExist:
            message = "the file does not exists"
            explanation = "the voice file does not exists"

            return response.Response({"message": message, "explanation": explanation}, status=412)
        except db.utils.IntegrityError:
            result_str = ''.join((choice('abcdefghijklmnopqrstuvwxyz') for i in range(4)))
            voice = models.Voice.objects.get(pk=self.kwargs['pk'])
            old_file_path = voice.voice_file.path
            file_name_list = request.data['file_name'].split('.')
            name = f"{file_name_list[0]}_{result_str}.{file_name_list[-1]}"
            voice.file_name = name
            voice.voice_file = f"voices/{name}"
            voice.save()
            rename(old_file_path, f"media/voices/{name}")
            message = "the voice updated"
            explanation = "the voice has been updated successfully"

            return response.Response({"message": message, "explanation": explanation}, status=200)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def destroy(self, request, *args, **kwargs):
        try:
            if ',' in self.kwargs['pk']:
                keys = self.kwargs['pk'].split(',')
                for key in keys:
                    key = int(key)
                    models.Voice.objects.get(pk=key).delete()

                message = "the voices deleted"
                explanation = "the voice files has been deleted successfully"

                return response.Response({"message": message, "explanation": explanation}, status=200)
            else:
                models.Voice.objects.get(pk=self.kwargs['pk']).delete()
                message = "the voice deleted"
                explanation = "the voice has been deleted successfully"

                return response.Response({"message": message, "explanation": explanation}, status=200)
        except core.exceptions.ObjectDoesNotExist:
            message = "the file does not exists"
            explanation = "the voice file does not exists"

            return response.Response({"message": message, "explanation": explanation}, status=412)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)


class CRUDImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all().order_by('publish_date')
    serializer_class = serializers.ImageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = self.queryset
        # user = User.objects.get(username=self.request.user.username)
        user = contrib.auth.models.User.objects.get(username=getenv('DJANGO_SUPERUSER_USERNAME'))
        query_set = queryset.filter(user=user)
        return query_set

    def list(self, request, *args, **kwargs):
        try:
            images = models.Image.objects.all()
            image_serializer = serializers.ImageSerializer(images, many=True)
            return response.Response(image_serializer.data, status=200)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def create(self, request, *args, **kwargs):
        try:
            # user = User.objects.get(username=request.user.username)
            user = contrib.auth.models.User.objects.get(username=getenv('DJANGO_SUPERUSER_USERNAME'))
            image = models.Image.objects.create(image_file=request.data['image_file'],
                                                user=user)
            image.save()
            image.file_name = str(image.image_file).split('/')[-1]
            image.save()
            message = "the image created"
            explanation = "the image has been created successfully"

            return response.Response({"message": message, "explanation": explanation}, status=201)

        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def update(self, request, *args, **kwargs):
        try:
            image = models.Image.objects.get(pk=self.kwargs['pk'])
            old_path = image.image_file.path
            image.file_name = request.data['file_name']
            image.image_file = f"images/{request.data['file_name']}"
            image.save()
            rename(old_path, f"media/images/{request.data['file_name']}")
            message = "the image updated"
            explanation = "the image has been updated successfully"

            return response.Response({"message": message, "explanation": explanation}, status=200)

        except db.utils.IntegrityError:
            result_str = ''.join((choice('abcdefghijklmnopqrstuvwxyz') for i in range(4)))
            image = models.Image.objects.get(pk=self.kwargs['pk'])
            old_file_path = image.image_file.path
            file_name_list = request.data['file_name'].split('.')
            name = f"{file_name_list[0]}_{result_str}.{file_name_list[-1]}"
            image.file_name = name
            image.image_file = f"images/{name}"
            image.save()
            rename(old_file_path, f"media/images/{name}")
            message = "the image updated"
            explanation = "the image has been updated successfully"

            return response.Response({"message": message, "explanation": explanation}, status=200)

        except core.exceptions.ObjectDoesNotExist:
            message = "the file does not exists"
            explanation = "the image file does not exists"

            return response.Response({"message": message, "explanation": explanation}, status=412)

        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def destroy(self, request, *args, **kwargs):
        try:
            if ',' in self.kwargs['pk']:
                keys = self.kwargs['pk'].split(',')
                for key in keys:
                    key = int(key)
                    models.Image.objects.get(pk=key).delete()

                message = "the images deleted"
                explanation = "the image files has been deleted successfully"

                return response.Response({"message": message, "explanation": explanation}, status=200)
            else:
                models.Image.objects.get(pk=self.kwargs['pk']).delete()
                message = "the image deleted"
                explanation = "the image has been deleted successfully"

                return response.Response({"message": message, "explanation": explanation}, status=200)
        except core.exceptions.ObjectDoesNotExist:
            message = "the file does not exists"
            explanation = "the image file does not exists"

            return response.Response({"message": message, "explanation": explanation}, status=412)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)


class CRUDVideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all().order_by('publish_date')
    serializer_class = serializers.VideoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = self.queryset
        # user = User.objects.get(username=self.request.user.username)
        user = contrib.auth.models.User.objects.get(username=getenv('DJANGO_SUPERUSER_USERNAME'))
        query_set = queryset.filter(user=user)
        return query_set

    def list(self, request, *args, **kwargs):
        try:
            videos = models.Video.objects.all()
            video_serializer = serializers.VideoSerializer(videos, many=True)
            return response.Response(video_serializer.data, status=200)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def create(self, request, *args, **kwargs):
        try:
            # user = User.objects.get(username=request.user.username)
            user = contrib.auth.models.User.objects.get(username=getenv('DJANGO_SUPERUSER_USERNAME'))
            video = models.Video.objects.create(video_file=request.data['video_file'],
                                                user=user)
            video.save()
            video.file_name = str(video.video_file).split('/')[-1]
            video.save()
            message = "the video created"
            explanation = "the video has been created successfully"

            return response.Response({"message": message, "explanation": explanation}, status=201)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def update(self, request, *args, **kwargs):
        try:
            video = models.Video.objects.get(pk=self.kwargs['pk'])
            old_path = video.video_file.path
            video.file_name = request.data['file_name']
            video.video_file = f"videos/{request.data['file_name']}"
            video.save()
            rename(old_path, f"media/videos/{request.data['file_name']}")
            message = "the video updated"
            explanation = "the video has been updated successfully"

            return response.Response({"message": message, "explanation": explanation}, status=200)
        except core.exceptions.ObjectDoesNotExist:
            message = "the file does not exists"
            explanation = "the video file does not exists"

            return response.Response({"message": message, "explanation": explanation}, status=412)
        except db.utils.IntegrityError:
            result_str = ''.join((choice('abcdefghijklmnopqrstuvwxyz') for i in range(4)))
            video = models.Video.objects.get(pk=self.kwargs['pk'])
            old_file_path = video.video_file.path
            file_name_list = request.data['file_name'].split('.')
            name = f"{file_name_list[0]}_{result_str}.{file_name_list[-1]}"
            video.file_name = name
            video.video_file = f"videos/{name}"
            video.save()
            rename(old_file_path, f"media/videos/{name}")
            message = "the video updated"
            explanation = "the video has been updated successfully"

            return response.Response({"message": message, "explanation": explanation}, status=200)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)

    def destroy(self, request, *args, **kwargs):
        try:
            if ',' in self.kwargs['pk']:
                keys = self.kwargs['pk'].split(',')
                for key in keys:
                    key = int(key)
                    models.Video.objects.get(pk=key).delete()

                message = "the videos deleted"
                explanation = "the video files has been deleted successfully"

                return response.Response({"message": message, "explanation": explanation}, status=200)
            else:
                models.Video.objects.get(pk=self.kwargs['pk']).delete()
                message = "the video deleted"
                explanation = "the video has been deleted successfully"

                return response.Response({"message": message, "explanation": explanation}, status=200)
        except core.exceptions.ObjectDoesNotExist:
            message = "the file does not exists"
            explanation = "the video file does not exists"

            return response.Response({"message": message, "explanation": explanation}, status=412)
        except Exception as exception:
            return response.Response(data=f"error: {str(exception.__class__)}", status=400)
