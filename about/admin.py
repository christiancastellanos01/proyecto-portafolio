from django.contrib import admin
from .models import Academic, Skill
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register([Academic, Skill], AboutAdmin)
