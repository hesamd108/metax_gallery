import json

from django.http import JsonResponse


class DataValidatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            response = self.get_response(request)
            if not request.FILES:
                response.data['message'] = "not null"
                response.data['explanation'] = "voice file could not be null, please upload a valid voice file"
                response.content = json.dumps(response.data)
                response.status_code = 422
                return response
            match request.FILES:
                case _ if 'voice_file' in request.FILES:
                    extension = request.FILES['voice_file'].name.split('.')[-1]
                    if extension not in ['mp3', 'wav', 'ogg', 'flac', 'aac']:
                        response.data['message'] = "invalid input type"
                        response.data['explanation'] = "voice file is not valid, use a valid file"
                        response.content = json.dumps(response.data)
                        response.status_code = 422
                        return response
                    return response

                case _ if 'image_file' in request.FILES:
                    extension = request.FILES['image_file'].name.split('.')[-1]
                    if extension not in ['jpg', 'jpeg', 'png']:
                        response.data['message'] = "invalid input type"
                        response.data['explanation'] = "image file is not valid, use a valid file"
                        response.content = json.dumps(response.data)
                        response.status_code = 422
                        return response
                    return response

                case _ if 'video_file' in request.FILES:
                    extension = request.FILES['video_file'].name.split('.')[-1]
                    if extension not in ['wmv', 'mov', 'mp4', 'avi']:
                        response.data['message'] = "invalid input type"
                        response.data['explanation'] = "video file is not valid, use a valid file"
                        response.content = json.dumps(response.data)
                        response.status_code = 422
                        return response
                    return response

                case _:
                    return response
        elif request.method == "PUT":
            data = json.loads(request.body)
            if 'file_name' not in data:
                message = "invalid input type"
                explanation = "use file_name in PUT request body"

                return JsonResponse({"message": message, "explanation": explanation}, status=422)
            if not data['file_name']:
                message = "not null"
                explanation = "the file_name cannot be empty"
                return JsonResponse({"message": message, "explanation": explanation}, status=422)
            return self.get_response(request)
        else:
            return self.get_response(request)
