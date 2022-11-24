# from django.contrib import admin
from django.urls import path
from app.views import home, contato, painel

urlpatterns = [
    # path('', admin.site.urls),
    path('', home),
    path('contato/', contato),
    path('painel/', painel),
]
