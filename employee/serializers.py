import re
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Check if the e-mail is from luizalabs
    """
    def validate_email(self, value):
        if not re.match(r"^\w[\w\.\-\_]+@luizalabs\.com$", value):
            raise serializers.ValidationError("Only luizalabs e-mails are allowed")
        return value

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')