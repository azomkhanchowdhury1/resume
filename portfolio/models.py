from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=500, help_text="Comma separated tech stack (e.g. Django, Python, HTML)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_tech_stack_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"
