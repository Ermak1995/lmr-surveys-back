from .models import Person, Surveys
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    # def create(self, validated_data):
    #     return Person.objects.create(**validated_data)


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveys
        fields = '__all__'

    # def create(self, validated_data):
    #     return Surveys.objects.create(**validated_data)
