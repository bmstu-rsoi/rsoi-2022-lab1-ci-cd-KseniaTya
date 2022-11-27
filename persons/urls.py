from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.persons, name='persons'),
    path('persons/<person_id>', views.person, name='person'),
    path('create_person/', views.create_person, name='create_person'),
    path('update_person/<person_id>', views.update_person, name='update_person'),
    path('delete_person/<person_id>', views.delete_person, name='delete_person'),
]
