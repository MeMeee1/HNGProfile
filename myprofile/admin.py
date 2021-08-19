from django.contrib import admin
from .models import New


@admin.register(New)
class ResponseAdmin(admin.ModelAdmin):
	pass


# Register your models here.
