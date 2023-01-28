from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/persons/', views.persons_operations, name='persons'),
    path('api/v1/persons/<int:pk>', views.person_id_operations, name='persons_id'),
]
