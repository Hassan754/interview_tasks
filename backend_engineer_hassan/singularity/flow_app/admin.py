from django.contrib import admin

from .models import FlowCalculation


@admin.register(FlowCalculation)
class FlowCalculationAdmin(admin.ModelAdmin):
    list_display = ("active_power", "reactive_power", "created")
    ordering = ("-created",)
