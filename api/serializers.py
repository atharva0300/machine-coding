from decimal import Decimal

from rest_framework import serializers

from .models import Department


class Limits:
    NAME_MAX_LENGTH = 100
    DESIGNATION_MAX_LENGTH = 100
    SALARY_MAX_DIGITS = 12
    SALARY_DECIMAL_PLACES = 2
    SALARY_MIN = Decimal("0.01")


class CreateEmployeeRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=Limits.NAME_MAX_LENGTH)
    email = serializers.EmailField()
    department = serializers.ChoiceField(choices=[d.value for d in Department])
    designation = serializers.CharField(max_length=Limits.DESIGNATION_MAX_LENGTH)
    salary = serializers.DecimalField(
        max_digits=Limits.SALARY_MAX_DIGITS,
        decimal_places=Limits.SALARY_DECIMAL_PLACES,
        min_value=Limits.SALARY_MIN,
    )
    joining_date = serializers.DateField()


class EmployeeResponseSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    department = serializers.CharField(source="department.value")
    designation = serializers.CharField()
    salary = serializers.DecimalField(
        max_digits=Limits.SALARY_MAX_DIGITS, decimal_places=Limits.SALARY_DECIMAL_PLACES
    )
    joining_date = serializers.DateField()
