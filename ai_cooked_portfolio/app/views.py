from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import redirect, render
from rest_framework import generics

from .models import ContactMessage, Project
from .serializers import ContactSerializer, ProjectSerializer


def home(request):
    return render(request, "index.html", {"projects": Project.objects.all()})


def download_resume(request):
    path = Path(settings.BASE_DIR) / "static" / "resume" / "Kankunala_Yamini_Resume.docx"
    if not path.exists():
        raise Http404("Resume not found")
    return FileResponse(open(path, "rb"), as_attachment=True, filename="Kankunala_Yamini_Resume.docx")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        text = request.POST.get("message", "").strip()
        if name and email and text:
            ContactMessage.objects.create(name=name, email=email, message=text)
            messages.success(request, "Thanks! Your message was sent.")
        else:
            messages.error(request, "Please fill in all three fields.")
    return redirect("/#contact")


def profile_api(request):
    return JsonResponse({
        "name": "Kankunala Yamini",
        "role": "Backend / Full-stack (fresher)",
        "stack": ["Python", "Django", "REST API", "MySQL"],
        "learning": "AI agents",
        "open_to_work": True,
    })


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContactCreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
