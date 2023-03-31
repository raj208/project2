from django.contrib import admin
from .models import Team
admin.site.register(Team)

# Register your models here.
def __str__(self):
    return self.first_name