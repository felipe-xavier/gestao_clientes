from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


@login_required
def clientes_list(request):
    people = Person.objects.all()
    return render(request, 'people.html', {'people': people})


@login_required
def clientes_new(request):
    form = PersonForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')
        
    return render(request, 'new_cliente_form.html', {'form': form})


@login_required
def clientes_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')

    return render(request, 'new_cliente_form.html', {'form': form})


@login_required
def clientes_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('clientes_list')

    return render(request, 'confirm_delete_form.html', {'person': person})