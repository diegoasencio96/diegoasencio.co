from django.shortcuts import render
from .models import SiteConfig, SocialNetwork, AboutMe, Service, Entrepreneurial, ProfessionalSkill, TechnicalSkill, ClientReview

# Create your views here.


def index(request):
    context = {
        'site_config': SiteConfig.objects.first(),
        'social_networks': SocialNetwork.objects.all(),
        'about_me': AboutMe.objects.first(),
        'services': Service.objects.all(),
        'features_projects': Entrepreneurial.objects.all(),
        'professional_skills': ProfessionalSkill.objects.all(),
        'technical_skills': TechnicalSkill.objects.all(),
        'client_reviews': ClientReview.objects.all(),
    }
    return render(request, 'landing/index.html', context=context)
