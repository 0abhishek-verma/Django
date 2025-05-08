from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cards
# Create your views here.
def home(request):
    return render(request,'firstapp/index.html')
def form(request):
    if request.method == 'GET':
        return render(request,'firstapp/form.html')
    if request.method == 'POST':
        title = request.POST.get('title')
        des = request.POST.get('des')
        # likes = request.POST.get('likes')
        # readtime = request.POST.get('readtime')
        Cards.objects.create(title=title,description=des)
        return render(request,'firstapp/form.html',{'title':title,'des':des})
def cards(request):
    mycard = Cards.objects.all()
    return render(request,'firstapp/cards.html',{'mycard':mycard})

def update(request,id):
    if request.method == 'GET':
        card = Cards.objects.filter(id=id)
        if not card:
            return HttpResponse('Card not found')
        card = Cards.objects.get(id=id)
        return render(request,'firstapp/update.html',{'card':card})
    if request.method == 'POST':
        card = Cards.objects.filter(id=id)
        if not card:
            return HttpResponse('Card not found')
        card = Cards.objects.get(id=id)
        title = request.POST.get('title')
        des = request.POST.get('des')
        card.title = title
        card.description = des
        card.save()
        return redirect('/cards/')
def delete(request,id):
    card = Cards.objects.filter(id=id)
    if not card:
        return HttpResponse('Card not found')
    card = Cards.objects.get(id=id)
    card.delete()
    return redirect('/cards/')