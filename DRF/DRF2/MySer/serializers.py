from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(label='姓名', max_length=20)
    age = serializers.IntegerField(label='年龄')
    score = serializers.IntegerField(label='分数')