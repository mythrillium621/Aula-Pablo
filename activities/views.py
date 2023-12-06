from django.shortcuts import render, redirect, reverse
from .models import Activity
from .forms import ActivityForm

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

def activity_delete(request, id):
    activity = Activity.objects.get(id=id)

    if request.method == 'POST':
        activity.delete()
        # messages.success(request, f'Atividade "{activity.name}" deletada com sucesso!')
        return redirect('activity_list')


    # return render(request, 'activities/activity_delete.html', context)


