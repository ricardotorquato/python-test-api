from django.db import models

class Employee(models.Model):
    """
    Employee Model
    """
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' from ' + self.department + ' department (' + self.email + ')'