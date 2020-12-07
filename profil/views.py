from django.shortcuts import render
from .models import TechSkill, SoftSkill, Profession, ProfessionInfo, UserInfo


def index(request):
    skills = TechSkill.objects.all()
    softskills = SoftSkill.objects.all()
    professions = Profession.objects.all()
    infos = ProfessionInfo.objects.all()
    users = UserInfo.objects.all()
    context = {
        'softskills': softskills,
        'skills': skills,
        'professions': professions,
        'infos': infos,
        'users': users,
    }
    return render(request, 'profil/index.html', context)