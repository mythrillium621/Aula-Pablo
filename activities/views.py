from django.shortcuts import render, redirect
from .models import Activity
from .forms import ActivityForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activities/activity_list.html', {'activities': activities})

def activity_edit(request, id):
    activity = Activity.objects.get(id=id)
    form = ActivityForm(request.POST, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
        
    else:
        form = ActivityForm(instance=activity)

    context = {
        'form': form,
        'title': 'Editar Atividade',
        'name': activity.name,
        'hours': activity.hours_spent,
        'minutes': activity.minutes_spent,
        'button': 'Salvar',
                }
    
    return render(request, 'activities/activity_form.html', context)

def activity_new(request):
    form = ActivityForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    
    context = {
        'form': form,
        'title': 'Adicionar Atividade',
        'button': 'Adicionar',
    }
    return render(request, 'activities/activity_form.html', context)

class ActivityDelete(DeleteView):
    model = Activity
    fields = ['name', 'hours_spent', 'minutes_spent']
    success_url = reverse_lazy("activity_list")


