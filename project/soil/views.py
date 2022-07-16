from soil.models import User_Login
from django.shortcuts import render, HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'soil/home.html')

def crop(request):
    return render(request, 'soil/crop.html', {'title': 'Crop'})

def fertiliser(request):
    return render(request, 'soil/fertiliser.html', {'title': 'Fertiliser'})


def user(request):
    return render(request, 'soil/user-login.html', {'title': 'User Login'})
    
def trial(request):
    return render(request, 'soil/trial.html')


def register(request):
    if request.method == 'post':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phonenumber = request.POST['phonenumber']
        emailid = request.POST['emailid']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        pin = request.POST['pin']
        User_Login(fname = fname, lname = lname, phonenumber = phonenumber, emailid = emailid, username = username, password1 = password1, password2 = password2, state = state, city = city, address = address, pin = pin).save()
        msg="User Registration Successful"
        return render(request,'soil/register.html', {'title': 'Register'}, {'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

