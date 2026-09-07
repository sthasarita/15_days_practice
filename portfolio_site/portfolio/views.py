from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Experience, Training, Project

PROFILE = {
    "name": "Sarita Shrestha",
    "title": "Computer Student at Patan Multiple Campus",
    "tagline": "Building Skills in Python, SQL and Data Analytics | Aspiring Data Scientist",
    "bio": """I am a fourth-semester B.Sc. CSIT student at Patan Multiple Campus with a strong interest in Data Science and Data Analytics. I enjoy learning new technologies and continuously improving my technical skills through coursework, hands-on practice, and personal projects.
Currently, I am building my foundation in Python, SQL, Statistics, and Data Analytics, with the goal of becoming a skilled Data Scientist who can solve real-world problems using data.
Beyond academics, I believe that discipline, consistency, and continuous learning are the keys to long-term success. I enjoy reading books, exploring new ideas, and challenging myself to grow both personally and professionally.
I am always eager to learn, collaborate, and explore opportunities that help me develop my skills and contribute to meaningful projects.""",
    "location": "Lalipur, Nepal",
    "email": "shresthasarita28913@gmail.com",
    "phone": "9768788595",
    "socials": {
        "github": "https://github.com/sthasarita",
        "linkedin": "https://linkedin.com/in/sarita-shrestha-908967362",
        "twitter": "",
    },
    "skills": ["Python", "Django", "Pandas", "Matplolib", "Numpy","HTML/CSS", "SQL", "Git"],
}


def home(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('home')
        else:
            messages.error(request, "Please fix the errors below and resubmit.")

    context = {
        "profile": PROFILE,
        "experiences": Experience.objects.all(),
        "trainings": Training.objects.all(),
        "projects": Project.objects.all(),
        "form": form,
    }
    return render(request, "portfolio/index.html", context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project, "profile": PROFILE})