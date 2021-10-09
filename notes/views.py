from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import notesupdate
from .models import notes
# Create your views here.
def note(request):
    context ={'notes':notes.objects.all()}
    return render(request,'notes/home_note.html',context)

def add(request):
  form = notesupdate()
  if(request.method=='POST'):
    form = notesupdate(request.POST,)
    if form.is_valid():
      form.save()
      messages.success(request,'Notes succesfully created')
      return redirect('home_note')
  else:
    form = notesupdate()
  context = {'form':form}
  return render(request,'notes/add.html',context)

def delete(request,note_id):
  if request.method == 'POST':
    print(request.POST)
    ele = notes.objects.get(id=note_id)
    ele.delete()
    messages.info(request,"Notes Removed")
    return redirect('home_note')