from django.contrib import admin

from .models import Voice, Image, Video


class VoiceFileName(Voice):
    class Meta:
        proxy = True


class ImageFileName(Image):
    class Meta:
        proxy = True


class VideoFileName(Video):
    class Meta:
        proxy = True


class VoiceAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class VoiceFileNameAdmin(admin.ModelAdmin):
    exclude = ('publish_date', 'voice_file', 'user',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ImageAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class ImageFileNameAdmin(admin.ModelAdmin):
    exclude = ('publish_date', 'image_file', 'user',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class VideoAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class VideoFileNameAdmin(admin.ModelAdmin):
    exclude = ('publish_date', 'video_file', 'user',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Voice, VoiceAdmin)
admin.site.register(VoiceFileName, VoiceFileNameAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageFileName, ImageFileNameAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoFileName, VideoFileNameAdmin)
