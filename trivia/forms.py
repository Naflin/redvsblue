from django import forms

class TriviaAnswerForm(forms.Form):
    query = forms.CharField()