from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import MaskCreatorForm, SignUpForm, SupportForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BrandMasks, MaskCreator, SupportModel
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

# Create your views here.
def home(request):
  return render(request, "home.html")

def login(request):
  return render(request, "registration/login.html")

def success(request):
  return render(request,"success.html")

def successcomment(request):
  return render(request,'successcomment.html')

def userdata(request):
  return render(request,"datos.html")

def support(request):
    if request.method=='POST':
        form = SupportForm(request.POST)
        print("here?")
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('sent')
    else:
        initial = {'usuario':request.user.username}
        form = SupportForm(initial=initial)

    return render(request, 'soporte.html', {'form': form})

class UserBoard(ListView):
    model = MaskCreator
    template_name = "userboard.html"

class ViewMasksSport(ListView):
    model = BrandMasks
    template_name = "sport.html"

class ViewMasksKids(ListView):
    model = BrandMasks
    template_name = "kids.html"

class ViewMasksCasual(ListView):
    model = BrandMasks
    template_name = "casual.html"

class ViewMasksRar(ListView):
    model = BrandMasks
    template_name = "different.html"

def CreateMask(request):
    if request.method=='POST':
        form = MaskCreatorForm(request.POST)
        print("here?")
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('userboard')
    else:
        initial = {'usuario':request.user.username}
        form = MaskCreatorForm(initial=initial)

    return render(request, 'create.html', {'form': form})

def buscar(request):
  if request.method == "POST":
    searched = request.POST['searched']
    mask_id = BrandMasks.objects.filter(marca__icontains=searched)
    return render(request,'search.html',{'searched':searched,'brandmasks':mask_id})
  else:
    return render(request,'not_found.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucess')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})