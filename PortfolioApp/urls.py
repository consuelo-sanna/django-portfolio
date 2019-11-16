from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('experience',views.experience, name="experience" ),
    path('education',views.education, name="education" ),
    path('skill',views.skill, name="skill" ),

]
