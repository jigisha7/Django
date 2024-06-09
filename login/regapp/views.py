from django.shortcuts import render

# Create your views here.
def userreg(request):
    return render(request,"/template/userreg.html",{})

