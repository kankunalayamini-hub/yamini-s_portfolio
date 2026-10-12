from django.test import TestCase
from .models import Project


class HomeTests(TestCase):
    def test_home_page_loads(self):
        Project.objects.create(title="Demo", problem="p", built="b", role="r", tags="Python, Django")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Demo")

    def test_projects_api(self):
        self.assertEqual(self.client.get("/api/projects/").status_code, 200)
