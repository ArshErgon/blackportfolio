from django.shortcuts import render, redirect

from .models import SkillModel, AboutModel, LearntModel, SeoModel, Project, SocialMedia

def home(request):
    skills = SkillModel.objects.all()
    abouts = AboutModel.objects.all()
    learnt = LearntModel.objects.all()
    seos = SeoModel.objects.all()
    media = projects = ""
    for media in SocialMedia.objects.all():
        pass
    ab = seo = lt = ab = sk = ""
    for sk in skills:
        pass
    for lt in learnt:
        pass
    for sk in skills:
        pass
    for seo in seos:
        pass
    for ab in abouts:
        pass
        
    return render(request, 'home/index.html', {'sk':sk, 'ab':ab, 'lt':lt, 'seo':seo, 'projects':Project.objects.all(), 'media':media})