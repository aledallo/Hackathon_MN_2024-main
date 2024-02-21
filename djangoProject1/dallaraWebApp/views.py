from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return render(request,"htmls/login.html")
    else:
        return render(request,"htmls/login.html")
# Create your views here.
def homepage_director(request):
    return HttpResponse("director")

def homepage_human_resources(request):
    return HttpResponse("human_resources")


def homepage_employee(request):
    return render(request, "htmls/homepage_employee.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if username in ["mic"]:
                return HttpResponseRedirect(reverse("employee"))
            else:
                return HttpResponseRedirect(reverse("login_view"))

        else:
            return render(request, "htmls/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "htmls/login.html")
