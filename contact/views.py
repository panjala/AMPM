from django.shortcuts import render

# Create your views here.i

def contact(request):
    return render(request,"contact.html")


def india(request):


    return render(request,"india.html")
def google_map(request):
    return render(request,"google_map.html")
