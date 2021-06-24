from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nam = fm.cleaned_data['name']
            mail = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(name = nam ,email = mail ,password= pas)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stude = User.objects.all()

    return render(request,'enroll/addShow.html',{'form' : fm, 'stud':stude})

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST , instance=pi)
        if fm.is_valid:
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request,'enroll/update.html',{'form':fm})


def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')