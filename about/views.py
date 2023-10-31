from django.shortcuts import render
from .models import Academic, Skill

# Create your views here.


def about(request):
    academic = Academic.objects.all()
    skill = Skill.objects.all()
    return render(request, 'about/about.html', {'academics': academic, 'skills': skill})
