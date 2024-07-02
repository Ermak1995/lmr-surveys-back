from .models import Surveys
from rest_framework import serializers
from .mongodb_utils import survey_collection


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveys
        fields = '__all__'

    # def create(self, validated_data):
    #     return Surveys.objects.create(**validated_data)
