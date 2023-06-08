from django.contrib import admin
from django.urls import path
from app.views import gpt3_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gpt3/', gpt3_view, name='gpt3'),
]
