from django.shortcuts import render


def home_page(request):
    return render(request, "about.html")


def experience(request):
    return render(request, "experience.html")


def education(request):
    return render(request, "education.html")


def skill(request):
    return render(request, "skill.html")


