from django.contrib import admin

from server.apps.main.models import DynamicHtml


@admin.register(DynamicHtml)
class DynamicHtmlAdmin(admin.ModelAdmin[DynamicHtml]):
    """Admin panel example for ``DynamicHtml`` model."""
