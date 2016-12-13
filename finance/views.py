from django.shortcuts import render
from . import generator
from .forms import ChargeForm

# Create your views here.

def base_page(request):
    return render(request, 'main.html')

def form(request):
    if request.method == "POST":
        form = ChargeForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
        else:
            pass
    else:
        form = ChargeForm()
    return render(request, 'form.html', {'form':form})

def generator_view(request):
    lst = [item for item in generator.random_transactions()]
    lst_plus = [item for item in lst if item[1] > 0]
    lst_minus = [item for item in lst if item[1] < 0]
    return render(request, 'generator.html', {'lst_plus':lst_plus, 'lst_minus':lst_minus})        
