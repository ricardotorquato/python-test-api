from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^employee/(?P<pk>[0-9]+)$',
        views.get_delete_employee,
        name='get_delete_employee'
    ),
    url(
        r'^employee/$',
        views.get_post_employees,
        name='get_post_employees'
    )
]