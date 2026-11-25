from django.urls import path

from .services import EmployeeService
from .storage import InMemoryStore
from .views import CreateEmployeeView


def build_urlpatterns():
    employee_service = EmployeeService(InMemoryStore())
    return [
        path("employees", CreateEmployeeView.as_view(employee_service=employee_service)),
    ]


urlpatterns = build_urlpatterns()
