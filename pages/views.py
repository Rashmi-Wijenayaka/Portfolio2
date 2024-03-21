from django.shortcuts import render

# The views for displaying something to a visitor.

def home(request):
    return render(request, "pages/home.html", {})
