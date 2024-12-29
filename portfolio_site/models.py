from django.db import models

# Contact form model to store submitted messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.sent_at}"

# Project model to list your projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    repo_url = models.URLField()
    live_url = models.URLField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
