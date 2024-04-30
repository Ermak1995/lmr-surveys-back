from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .forms import SearchSurvey
from .utils import db

from .serializers import PersonSerializer, SurveySerializer
from rest_framework import viewsets
from .models import Person, Surveys


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SurveysViewSet(viewsets.ModelViewSet):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer


@csrf_exempt
def create_survey(request):
    if request.method == 'GET':
        surveys = Surveys.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# class SurveyViewSet(viewsets.ModelViewSet):
#
#     queryset = Surveys.objects.all()
#     serializer_class = SurveySerializer


# def index(request):
#     form = SearchSurvey()
#     surveys = db['surveys']
#     all_surveys = surveys.find()
#     return render(request, 'home/index.html', {'form': form, 'all_surveys': all_surveys})
