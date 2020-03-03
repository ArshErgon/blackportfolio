from django.shortcuts import render, redirect

from .models import SkillModel, AboutModel, LearntModel, ContactModel, SeoModel

def home(request):
    skills = SkillModel.objects.all()
    abouts = AboutModel.objects.all()
    learnt = LearntModel.objects.all()
    seos = SeoModel.objects.all()
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

    # Contact me
    if request.method == 'POST':
        personName = request.POST.get('name')
        personEmail = request.POST.get('email')
        personNumber = request.POST.get('phNumber')
        ContactModel.objects.create(name=personName, email=personEmail, phnumber=personNumber)
        return redirect('/')
    return render(request, 'home/index.html', {'sk':sk, 'ab':ab, 'lt':lt, 'seo':seo})