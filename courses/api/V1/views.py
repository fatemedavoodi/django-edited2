from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Course
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializer import *



@api_view()
def course_api_view(request):
    courses = Course.objects.filter(status = True)
    courses_serializer = CourseApiSerializer(courses, many=True)
    return Response(courses_serializer.data)

@api_view()
def course_api_detail_view(request,pk):
    course = get_object_or_404(Course, id=pk)
    course_serializer = CourseApiSerializer(course)
    return Response(course_serializer.data)


