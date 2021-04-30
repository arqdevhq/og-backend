from django.urls import reverse

from rest_framework import serializers

from server.apps.main.models import DynamicHtml

class DynamicHtmlSerializer(serializers.ModelSerializer):

    dynamic_html_url = serializers.SerializerMethodField()

    class Meta:
        model = DynamicHtml
        fields = ['id', 'title', 'html_text', 'description', 'site_name', 
        'site_url', 'image_url', 'dynamic_html_url','created_at', 'updated_at']

    def get_dynamic_html_url(self, obj):
        if obj:
            return reverse('main:dynamic_html', kwargs={'pk':obj.id})
        return False