from rest_framework import serializers
from MySer.models import *
# class StudentSerializer(serializers.Serializer):
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(label='姓名', max_length=20)
    # age = serializers.IntegerField(label='年龄')
    # score = serializers.IntegerField(label='分数')
    class Meta:
        model = Student
        # fields = ('name', 'age', 'score')
        fields = '__all__'