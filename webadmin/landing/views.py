from django.shortcuts import render
from .models import SiteConfig, SocialNetwork, AboutMe, ProfessionalSkill

# Create your views here.


def index(request):
    context = {
        'site_config': SiteConfig.objects.first(),
        'social_networks': SocialNetwork.objects.all(),
        'about_me': AboutMe.objects.first(),
        'professional_skill': ProfessionalSkill.objects.all(),
    }
    return render(request, 'landing/index.html', context=context)
