from django.shortcuts import render, redirect
from .forms import IncidentsForm

def incident(request):

    return render(request, 'incident/incident.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = IncidentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верно заполнена'


    form =IncidentsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'incident/create.html', data)