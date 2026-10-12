from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    status = models.CharField(max_length=60, blank=True)
    problem = models.TextField()
    why = models.TextField(blank=True, help_text="Optional: why we built it")
    built = models.TextField()
    role = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, help_text="Comma separated, e.g. Python, Django")
    live_url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.email})"
