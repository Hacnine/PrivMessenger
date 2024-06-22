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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET'])
def course_info(request, id=None):
    if id is not None:
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    else:
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_course(request, id=None):
    serializer = CourseSerializer(data=request.data)
    serializer.save()
    response_message = {'msg': 'Successfully insert'}
    return Response(serializer.errors)


@api_view(['PUT', 'PATCH'])
def update_course(request, pk=None):
    try:
        # Attempt to get the course by primary key
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        # Return a 404 response if the course is not found
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    # Determine if this is a partial update (PATCH) or full update (PUT)
    partial = request.method == 'PATCH'

    # Initialize the serializer with the course instance and the incoming data
    serializer = CourseSerializer(course, data=request.data, partial=partial)

    # Validate and save the serializer
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Successfully updated'}, status=status.HTTP_200_OK)

    # Return validation errors if the serializer is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_course(request, pk=None):
    try:
        # Attempt to get the course by primary key
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({'msg': 'Successfully deleted'}, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        # Return a 404 response if the course is not found
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
