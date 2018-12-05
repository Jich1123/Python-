from rest_framework import serializers
from MySer.models import *
# class StudentSerializer(serializers.Serializer):
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.CharField(label='姓名', max_length=20)
    # age = serializers.IntegerField(label='年龄')
    # score = serializers.IntegerField(label='分数')
    class Meta:
        model = Studnet
        # fields = ('name', 'age', 'score')
        fields = '__all__'