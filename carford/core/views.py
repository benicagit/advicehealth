from django.shortcuts import render

from .forms import ProprietarioModelForm, VeiculoModelForm

def indexView(request):
   return render(request, 'index.html')


def cadastroView(request):
    return render(request, 'cadastro.html')

