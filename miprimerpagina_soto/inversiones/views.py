from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
#from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'inversiones/index.html')