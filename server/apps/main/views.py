from django.http import HttpRequest, HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from server.apps.main.models import DynamicHtml
from server.apps.main.serializers import DynamicHtmlSerializer


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'main/index.html')


class DynamicHTMLDetailView(DetailView):
    model = DynamicHtml
    template_name = 'main/dynamic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        context.update({
            'title': obj.title,
            'description':  obj.description,
            'site_name': obj.site_name,
            'site_url': obj.site_url,
            'image_url': obj.image_url,
        })
        return context


class DynamicHTMLListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = DynamicHtml.objects.all()
    serializer_class = DynamicHtmlSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)