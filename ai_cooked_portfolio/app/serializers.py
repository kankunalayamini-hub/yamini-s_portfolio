from rest_framework import serializers
from .models import ContactMessage, Project


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "title", "status", "problem", "why", "built", "role", "tags", "live_url", "code_url"]

    def get_tags(self, obj):
        return obj.tag_list()


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
