from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['teacher_name', 'student_name', 'course_duration', 'seat']

    # {"teacher_name": "abn", "student_name": "SHS", "course_duration": 6, "seat": 45}

    # def create(self, validated_data):
    #     return Course.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
    #     instance.student_name = validated_data.get('student_name', instance.student_name)
    #     instance.course_duration = validated_data.get('course_duration', instance.course_duration)
    #     instance.seat = validated_data.get('seat', instance.seat)
    #
    #     instance.save()
    #     return instance

# from rest_framework import serializers
# from .models import Course

# class CourseSerializer(serializers.Serializer):
#     teacher_name = serializers.CharField(max_length=50)
#     student_name = serializers.CharField(max_length=50)
#     course_duration = serializers.IntegerField()
#     seat = serializers.IntegerField()

#     def create(self, validated_data):
#         return Course.objects.create(validated_data)
