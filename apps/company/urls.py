from django.urls import path
from .views import CompanyCreate, EditCompnay

urlpatterns = [
    path('new', CompanyCreate.as_view(), name="create_company"),
    path('edit/<int:pk>/', EditCompnay.as_view(), name="edit_company"),
]
