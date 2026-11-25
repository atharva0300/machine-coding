from django.urls import path

from .services import Service
from .storage import InMemoryStore


def build_urlpatterns():
    service = Service(InMemoryStore())
    return []


urlpatterns = build_urlpatterns()
