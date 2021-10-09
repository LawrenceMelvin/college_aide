from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import awareform
# Create your views here.
def index(request):
    return render(request,'awareness/index.html')

def aware(request):
    form = awareform()
    if request.method == 'POST':
        form = awareform(request.POST)
        if form.is_valid():
            person = form.cleaned_data['person']
            want = form.cleaned_data['wanted']
            print(want)
            if('placement' in want):
                print("PLACEMENT")
            return redirect('index')
    
    context={'form':form}
    return render(request,'awareness/aware.html',context)