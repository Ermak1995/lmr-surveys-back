from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'surveys', views.SurveysViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create-survey/', views.create_survey),
]