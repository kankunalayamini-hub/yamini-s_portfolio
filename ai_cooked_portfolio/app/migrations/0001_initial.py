from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("status", models.CharField(blank=True, max_length=60)),
                ("problem", models.TextField()),
                ("built", models.TextField()),
                ("role", models.CharField(max_length=200)),
                ("tags", models.CharField(help_text="Comma separated, e.g. Python, Django", max_length=200)),
                ("live_url", models.URLField(blank=True)),
                ("code_url", models.URLField(blank=True)),
                ("order", models.PositiveSmallIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
    ]
