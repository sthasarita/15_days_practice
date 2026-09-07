from django.db import models


class Experience(models.Model):
    role = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    duration = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Training(models.Model):
    title = models.CharField(max_length=150)
    provider = models.CharField(max_length=120, blank=True)
    year = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}>"