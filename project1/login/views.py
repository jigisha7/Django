from django.http import HttpResponse
from . models import Reguser
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home(request):
    #return render("Hello world")
    return render(request, 'home.html')

def userreg(request):
    return render(request, 'userreg.html')

def insertuser(request):
    vuid = request.POST['tuid']
    vuname = request.POST['tuname']
    vuemail = request.POST['tuemail']
    vucontact = request.POST['tucontact']
    us = Reguser(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact)
    us.save()
    return render(request, 'home.html', {})

def viewusers (request):
    user = Reguser.objects.all() #tablename
    return render(request, "viewusers.html",{'userdata':user})

def deleteprofile (request, id):
    #us = Reguser.objects.get(uid=id) #if we want to delete multiple record with same id get will give error so use filter method
    us = Reguser.objects.filter(uid=id)
    us.delete()
    return redirect("/viewusers")

def editprofile(request, id):
    # user = Reguser.objects.get(uid=id)
    # return render("/editprofile.html",{'user':user})
    user = get_object_or_404(Reguser, uid=id)  # Fetch the user object
    return render(request, 'editprofile.html', {'user': user})

def updateprofile(request, id):
    # Fetch the user object
    user = get_object_or_404(Reguser, uid=id)

    # Update the user object with new data from the POST request
    user.uid = request.POST['uid']
    user.uname = request.POST['uname']
    user.uemail = request.POST['uemail']
    user.ucontact = request.POST['ucontact']
    user.save()
    return redirect("/viewusers")