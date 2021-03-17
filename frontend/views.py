from django.shortcuts import render
import os

# Create your views here.
def index(request):
    
    debug = os.environ.get("DEBUG")
    print(debug)
    context = {
        "DEBUG": debug
    }
    return render(request, "frontend/index.html", context)
