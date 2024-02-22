from django.shortcuts import render
from item.models import Category, scenario

def index(request):
    scenarios = scenario.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'scenarios':scenarios,
    })
def contact(request):
    return render(request, 'core/contact.html')