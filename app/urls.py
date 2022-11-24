from django.contrib import admin
from django.urls import path
from app.views import view, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('contato/', contato),
]
