import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {'name': 'Alice'}
    context = {'foods': foods, 'info': info}
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발','햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)