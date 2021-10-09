from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import awareform
# Create your views here.
def index(request):
    return render(request,'awareness/index.html')

def aware(request):
    global all_page 
    form = awareform()
    if request.method == 'POST':
        form = awareform(request.POST)
        if form.is_valid():
            person = form.cleaned_data['person']
            want = form.cleaned_data['wanted']
            print(want)
            if('placement' in want and 'job' in want and 'skill' in want):
                all_page = 'all'
                return redirect('all')
            elif('placement' in want and 'job' not in want and 'skill' not in want):
                all_page='placement'
                return redirect('all')
            return redirect('index')
    
    context={'form':form}
    return render(request,'awareness/aware.html',context)

def all(request):
    if(all_page == 'all'):
        return render(request,'awareness/all.html')
    elif(all_page == 'placement'):
        return render(request,'awareness/placement.html')
    elif(all_page=='job'):
        return render(request,'awareness/job.html')
    else:
        return render(request,'awareness/code.html')