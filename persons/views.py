from django.shortcuts import render, redirect
from .models import Persons
from .forms import CreateUpdatePerson

def persons(request):
    persons = Persons.objects.all()
    context = {'persons': persons}
    return render(request, 'persons/persons.html', context)


def person(request, person_id):
    person = Persons.objects.get(id=person_id)
    context = {'person': person}
    return render(request, 'persons/person.html', context)


def create_person(request):
    form = CreateUpdatePerson()
    if request.method == 'POST':
        form = CreateUpdatePerson(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persons')
    context = {'form': form}
    return render(request, 'persons/create_person.html', context)


def update_person(request, person_id):
    person = Persons.objects.get(id=person_id)
    form = CreateUpdatePerson(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('persons')
    context = {'person': person, 'form': form}
    return render(request, 'persons/update_person.html', context)


def delete_person(request, person_id):
    person = Persons.objects.get(id=person_id)
    if request.POST:
        person.delete()
        return redirect('persons')
    context = {'person': person}
    return render(request, 'persons/delete_person.html', context)
