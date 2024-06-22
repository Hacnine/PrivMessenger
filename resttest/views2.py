
from django.shortcuts import render
import rest_framework
from .serializers import CourseSerializer
from .models import Course
from .serializers import CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import io
from rest_framework.parsers import JSONParser


def course_info(request):
    # complex data
    course = Course.objects.all()
    # python dict
    serializer = CourseSerializer(course, many=True)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to User
    return HttpResponse(json_data, content_type="application/json")


# Model instance

def single_course_info(request, pk):
    # complex data
    course = Course.objects.get(id=pk)
    # python dict
    serializer = CourseSerializer(course)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to User
    return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        json_data = request.body
        # json to stream
        stream = io.BytesIO(json_data)
        # stream to python
        python_data = JSONParser().parse(stream)
        # python to complex
        serializer = CourseSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_message = {'msg': 'Successful'}
            return JsonResponse(response_message)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        course_id = python_data.get('id')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)

        serializer = CourseSerializer(course, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response_message = {'msg': 'Successfully Updated.'}
            return JsonResponse(response_message)
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


def delete_course(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        course_id = python_data.get('id')
        get_data = Course.objects.get(id=id)
        get_data.delete()
        response_message = {'msg': 'Successfully Updated.'}
        return JsonResponse(response_message)

# @csrf_exempt
# def delete_course(request):
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         course_id = python_data.get('id')
#         get_data = Course.objects.get(id=course_id)
#         get_data.delete()
#         response_message = {'msg': 'Successfully Updated.'}
#         return JsonResponse(response_message)
