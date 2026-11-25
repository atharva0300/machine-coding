import logging

from django.urls import path

from .services import Service
from .storage import InMemoryStore
from .views import CreateView, ListView

logger = logging.getLogger(__name__)


def build_urlpatterns():
    service = Service(InMemoryStore())
    return [
        path("items", CreateView.as_view(service=service)),
        path("items/list", ListView.as_view(service=service)),
    ]


urlpatterns = build_urlpatterns()
