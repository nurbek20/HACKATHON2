from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Contact
from core.models import FoodCard, Category

# Create your views here.
def main(request):
    return render(request, 'index.html')

def message(request):
    if request.method == 'POST':
        send=Contact()
        send.email = request.POST.get("email")
        send.save()
        return HttpResponseRedirect('/')

def index(request):
    categories = Category.objects.all()
    foodCard = FoodCard.objects.all()
    context={'foodCard' :foodCard, 'categories' :categories}
    return render(request, 'index.html', context=context)