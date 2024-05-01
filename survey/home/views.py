from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .forms import SearchSurvey
from .utils import db
from uuid import uuid4

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
        uuid = str(uuid4())
        access_hash = str(uuid4())
        data = JSONParser().parse(request)
        data["uuid"] = uuid
        data["access_hash"] = access_hash
        print(data)
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def get_survey_by_uuid(request):
    uuid = request.GET["uuid"]
    obj = get_object_or_404(Surveys, uuid=uuid)
    serializer = SurveySerializer(obj)
    # print(serializer.data.get('survey'))
    survey = serializer.data.get('survey')
    # print(type(survey))
    return Response(survey)

# def index(request):
#     form = SearchSurvey()
#     surveys = db['surveys']
#     all_surveys = surveys.find()
#     return render(request, 'home/index.html', {'form': form, 'all_surveys': all_surveys})
