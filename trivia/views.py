from django.shortcuts import render
import requests

def home(request):
    response = requests.get("http://jservice.io/api/random")
    tridata = response.json()
    print(tridata)
    return render(request, 'trivia/home.html', {
        'id': tridata[0]['id'],
        'question': tridata[0]['question'],
        'answer': tridata[0]['answer'],
        'test': 'HEYYYY',
        'red': 0,
        'blue': 0,
    })
