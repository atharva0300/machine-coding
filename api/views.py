import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class CreateView(APIView):
    service = None

    def post(self, request):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


class ListView(APIView):
    service = None

    def get(self, request):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
