from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")


def Terms_Conditions(request):

    return render(request,"termscond.html")

