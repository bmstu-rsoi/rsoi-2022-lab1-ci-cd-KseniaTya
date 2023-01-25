from django.urls import path
from . import views

urlpatterns = [
    path('/api/v1/persons/', views.persons, name='persons'),
    path('/api/v1/persons/<person_id>', views.person, name='person'),
    path('/api/v1/create_person/', views.create_person, name='create_person'),
    path('/api/v1/update_person/<person_id>', views.update_person, name='update_person'),
    path('/api/v1/delete_person/<person_id>', views.delete_person, name='delete_person'),
]
