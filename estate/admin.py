from django.contrib import admin
from .models import Agent
from .models import About
from .models import Service
from .models import Properties
from .models import Index

admin.site.register(Agent)

admin.site.register(About)

admin.site.register(Service)

admin.site.register(Properties)

admin.site.register(Index)


# Register your models here.
