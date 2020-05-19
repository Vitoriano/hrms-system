from django.urls import path
from .views import EmployeeList

urlpatterns = [
    path('list', EmployeeList.as_view(), name="employee_list"),
]
