from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resume/", views.download_resume, name="resume"),
    path("contact/", views.contact, name="contact"),
    path("api/profile/", views.profile_api),
    path("api/projects/", views.ProjectList.as_view()),
    path("api/contact/", views.ContactCreate.as_view()),
]
