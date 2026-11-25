import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateEmployeeRequestSerializer, EmployeeResponseSerializer

logger = logging.getLogger(__name__)


class CreateEmployeeView(APIView):
    employee_service = None

    def post(self, request):
        logger.info("POST /api/employees")
        serializer = CreateEmployeeRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = self.employee_service.create_employee(**serializer.validated_data)
        return Response(EmployeeResponseSerializer(employee).data, status=status.HTTP_201_CREATED)
