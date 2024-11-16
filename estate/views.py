from django.shortcuts import render
from .models import Agent
from.models import Index
from .models import About
from .models import Service
from .models import Properties
from .models import Contact


from django.shortcuts import render

def index(request):
    index = Index.objects.first()
    return render(request, 'index.html', {'index': index})

# def index(request):
#     agents = Agent.objects.all()
#     return render(request, 'agents.html', {'agents': agents})


def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def properties(request):
    properties = Properties.objects.all()
    return render(request, 'properties.html', {'properties': properties})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # Save the contact information to the database
    return render(request, 'contact.html')

def agents(request):
    agents = Agent.objects.all()
    return render(request, 'agents.html', {'agents': agents})



# Create your views here.
