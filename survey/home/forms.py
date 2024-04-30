from django import forms


class SearchSurvey(forms.Form):
    survey_id = forms.IntegerField(label='id')
