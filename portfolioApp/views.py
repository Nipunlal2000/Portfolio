from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')

    linkedin_profile = Profile.objects.filter(about=about, social_name='linkedin').first()
    github_profile = Profile.objects.filter(about=about, social_name='github').first()

    categories = Category.objects.all()

    portfolios = Portfolio.objects.all()
    context = {
        'home': home,
        'about': about,
        'linkedin_profile': linkedin_profile,
        'github_profile': github_profile,
        'categories': categories,
        'portfolios': portfolios
    }

    return render(request, 'index.html', context)
