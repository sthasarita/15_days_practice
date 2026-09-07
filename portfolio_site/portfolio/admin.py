from django.contrib import admin
from .models import Experience, Training, Project, ContactMessage


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'duration', 'order')
    list_editable = ('order',)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'year', 'order')
    list_editable = ('order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)