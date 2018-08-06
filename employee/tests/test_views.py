import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Employee
from ..serializers import EmployeeSerializer


# initialize the APIClient app
client = Client()

class GetAllEmployeesTest(TestCase):
    """ Test module for get all employees with API """

    def setUp(self):
        Employee.objects.create(
            name='Arnaldo Pereira', email='arnaldo@luizalabs.com', department='Architecture')
        Employee.objects.create(
            name='Renato Pedigoni', email='renato@luizalabs.com', department='E-commerce')
        Employee.objects.create(
            name='Thiago Catoto', email='catoto@luizalabs.com', department='Mobile')

    def test_get_all_employees(self):
        # get API response
        response = client.get(reverse('get_post_employees'))
        # get data from db
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleEmployeeTest(TestCase):
    """ Test module for get a single employee with API """

    def setUp(self):
        self.arnaldo = Employee.objects.create(
            name='Arnaldo Pereira', email='arnaldo@luizalabs.com', department='Architecture')
        self.renato = Employee.objects.create(
            name='Renato Pedigoni', email='renato@luizalabs.com', department='E-commerce')
        self.catoto = Employee.objects.create(
            name='Thiago Catoto', email='catoto@luizalabs.com', department='Mobile')
    
    def test_get_valid_employee(self):
        # get API response
        response = client.get(
            reverse('get_delete_employee', kwargs={'pk': self.renato.pk}))
        # get data from db
        employee = Employee.objects.get(pk=self.renato.pk)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_invalid_employee(self):
        # get API response
        response = client.get(
            reverse('get_delete_employee', kwargs={'pk': 42}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class InsertEmployeeTest(TestCase):
    """ Test module for insert a employee with API """

    def setUp(self):
        self.valid = {
            'name': 'Arnaldo Pereira',
            'email': 'arnaldo@luizalabs.com',
            'department': 'Architecture',
        }
        self.invalid_blank = {
            'name': '',
            'email': '',
            'department': '',
        }
        self.invalid_email = {
            'name': 'Renato Pedigoni',
            'email': 'renato@qualquercoisa.com',
            'department': 'E-commerce',
        }
    
    def test_insert_valid_employee(self):
        # get API response
        response = client.post(
            reverse('get_post_employees'),
            data=json.dumps(self.valid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_insert_invalid_blank_employee(self):
        # get API response
        response = client.post(
            reverse('get_post_employees'),
            data=json.dumps(self.invalid_blank),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_insert_invalid_email_employee(self):
        # get API response
        response = client.post(
            reverse('get_post_employees'),
            data=json.dumps(self.invalid_email),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
class DeletingEmployeeTest(TestCase):
    """ Test module for deleting a employee with API """

    def setUp(self):
        self.arnaldo = Employee.objects.create(
            name='Arnaldo Pereira', email='arnaldo@luizalabs.com', department='Architecture')
        self.renato = Employee.objects.create(
            name='Renato Pedigoni', email='renato@luizalabs.com', department='E-commerce')
        self.catoto = Employee.objects.create(
            name='Thiago Catoto', email='catoto@luizalabs.com', department='Mobile')
    
    def test_delet_valid_employee(self):
        # get api response
        response = client.delete(
            reverse('get_delete_employee', kwargs={'pk': self.renato.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delet_invalid_employee(self):
        # get api response
        response = client.delete(
            reverse('get_delete_employee', kwargs={'pk': 42}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)