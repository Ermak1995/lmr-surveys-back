from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'surveys', views.SurveysViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-survey/', views.create_survey, name='create_survey'),
    path('survey', views.get_survey_by_uuid, name="get_survey"),
]
