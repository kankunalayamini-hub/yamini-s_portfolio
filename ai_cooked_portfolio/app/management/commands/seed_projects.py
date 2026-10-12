from django.core.management.base import BaseCommand
from app.models import Project

DATA = [
    dict(order=2, title="Educational Website", status="Live on Vercel",
         problem="Students need one place to browse courses and learning content.",
         built="A Django website with course pages, built with Django models, views and templates.",
         role="Solo project: backend, frontend and deployment.", tags="Python, Django, HTML, CSS",
         live_url="https://school-website-gules-nine.vercel.app/", code_url="https://github.com/kankunalayamini-hub"),
    dict(order=1, title="Employee Management System", status="Live on Vercel",
         problem="Small teams track employee records in spreadsheets, which gets messy.",
         built="A Django app to add, view, update and delete employee records.",
         role="Solo project: database models, views, templates and deployment.", tags="Python, Django, HTML, CSS",
         live_url="https://employee-managment-website.vercel.app/", code_url="https://github.com/kankunalayamini-hub"),
    dict(order=6, title="Healthcare API", status="REST API",
         problem="Healthcare data needs a clean, structured interface that other apps can use.",
         built="A REST API in Django to create, read, update and delete healthcare data. Only authorized users can access it.",
         role="Solo project: API design and implementation.", tags="Python, Django, REST API, Authorization",
         live_url="", code_url="https://github.com/kankunalayamini-hub"),
    dict(order=4, title="Meesho Website Redesign", status="Live on Vercel",
         problem="Practice turning a real e-commerce layout into a clean, responsive front end.",
         built="A responsive redesign that works on mobile and desktop, with JavaScript interactions.",
         role="Solo project: design and front-end code.", tags="HTML, CSS, Bootstrap, JavaScript",
         live_url="https://e-commerce-website-pied-eta.vercel.app/", code_url="https://github.com/kankunalayamini-hub"),
    dict(order=3, title="Adaptive Transaction Risk Scoring", status="Live on Vercel",
         problem="Fixed rules and labelled fraud data miss new fraud patterns and give only a yes/no answer, not a risk level.",
         why="To spot unusual transactions without labelled data, using unsupervised learning in a Flask app.",
         built="Our B.Tech final year project: it scores each transaction from 0 to 100 as low, medium or high risk.",
         role="Group project, built with my team.", tags="Python, Flask, scikit-learn, Pandas, Unsupervised ML",
         live_url="https://adaptive-transaction-risk-scoring-u.vercel.app/",
         code_url="https://github.com/kankunalayamini-hub/Adaptive-Transaction-risk-scoring-using-Unsupervised-learning"),
    dict(order=5, title="Trevour Travel Website", status="Live on Vercel",
         problem="Travellers need one place to explore destinations and plan a trip, on any device.",
         built="A responsive travel planning website with six destinations (Taj Mahal, Lotus Temple, Buddha Statue, Tea Plantations, Buckingham Palace, London Eye) and a validated trip planning form. It works on laptop, tablet and mobile.",
         role="Front-end project: HTML, CSS, Bootstrap and JavaScript.", tags="HTML, CSS, Bootstrap, JavaScript",
         live_url="https://trevour-travel-website.vercel.app/",
         code_url="https://github.com/kankunalayamini-hub/trevour-travel-website"),
]


class Command(BaseCommand):
    help = "Load Yamini's projects into the database"

    def handle(self, *args, **opts):
        for d in DATA:
            Project.objects.update_or_create(title=d["title"], defaults=d)
        self.stdout.write(self.style.SUCCESS(f"{len(DATA)} projects loaded"))
