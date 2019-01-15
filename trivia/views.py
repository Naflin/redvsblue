from django.shortcuts import render
import requests
from .forms import TriviaAnswerForm

def home(request):

    if 'trivia-obj' in request.session:
        tridata = request.session['trivia-obj']
    else:
        response = requests.get("http://jservice.io/api/random")
        tridata = response.json()
        request.session['trivia-obj'] = tridata

    form = TriviaAnswerForm()
    query = None
    if 'query' in request.GET:
        form = TriviaAnswerForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query == tridata[0]['answer']:
                response = requests.get("http://jservice.io/api/random")
                tridata = response.json()
                request.session['trivia-obj'] = tridata
            


    return render(request, 'trivia/home.html', {
        'form': form,
        'id': tridata[0]['id'],
        'question': tridata[0]['question'],
        'answer': tridata[0]['answer'],
        'test': 'HEYYYY',
        'red': 0,
        'blue': 0,
    })

def lobby(request):

    return render(request, 'trivia/lobby.html')