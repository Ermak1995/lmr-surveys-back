from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .forms import SearchSurvey
from .utils import db
from uuid import uuid4

from .serializers import SurveySerializer
from rest_framework import viewsets
from .models import Surveys


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
        # print(data)
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def get_survey_by_uuid(request):
    uuid = request.GET["uuid"]
    obj = get_object_or_404(Surveys, uuid=uuid)
    if request.method == 'GET':
        serializer = SurveySerializer(obj)
        # print(serializer.data.get('survey'))
        survey = serializer.data.get('survey')
        # print(type(survey))
        return Response(survey)
    elif request.method == 'DELETE':
        try:
            obj.delete()
        except:
            return Response('ERROR')
        return Response('The survey was successfully deleted')


@api_view(['GET', 'POST'])
def check_survey(request):
    uuid = request.GET["uuid"]
    survey = Surveys.objects.get(uuid=uuid).survey
    max_counter = counter = 0
    data = JSONParser().parse(request)
    for question in survey['questions']:
        max_counter += 1
        print(question)
        if question['correct_answer'] == data[question['id']]:
            counter += 1
    print(f'Ваш результат {counter} из {max_counter}')

    return JsonResponse({'counter': counter, 'max_counter': max_counter})

# def index(request):
#     form = SearchSurvey()
#     surveys = db['surveys']
#     all_surveys = surveys.find()
#     return render(request, 'home/index.html', {'form': form, 'all_surveys': all_surveys})
