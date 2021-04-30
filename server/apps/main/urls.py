from django.urls import path

from server.apps.main.views import index, DynamicHTMLListCreateAPIView, DynamicHTMLDetailView

app_name = 'main'

urlpatterns = [
    path('hello/', index, name='hello'),
    path('dynamic_html/<int:pk>/', DynamicHTMLDetailView.as_view(), name='dynamic_html'),
    path('api/dynamic_html/', DynamicHTMLListCreateAPIView.as_view(), name='dynamic_html_api')
]
