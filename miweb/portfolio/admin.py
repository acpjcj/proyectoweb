from django.contrib import admin
from .models import Project
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
# Register your models here.
# user cfernandez
# email cfernandez@fidesol.org
# password 12345678

# Crear un formulario personalizado para usar CKEditor5 en 'description'
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
                config_name="default"
            )
        }

# Extender el admin de Project usando el formulario personalizado
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title','content')
    date_hierarchy = 'published'
    list_filter = ('author','published')
    form = ProjectAdminForm  # Aplica el formulario aquí

# Registrar el modelo en el admin
admin.site.register(Project, ProjectAdmin)
