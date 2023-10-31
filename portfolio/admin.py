from django.contrib import admin
from .models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # esta clase se crea para poder mostrar en admin los campos que se hacen referencia en este caso como solo lectura


admin.site.register(Project, ProjectAdmin)
