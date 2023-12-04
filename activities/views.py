from django.shortcuts import render, redirect
from .models import Activity
from .forms import ActivityForm

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activities/activity_list.html', {'activities': activities})

def activity_edit(request, id):
    activity = Activity.objects.get(id=id)
    form = ActivityForm(request.POST or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    return render(request, 'activities/activity_form.html', {'form': form, 'title': 'Edit Activity'})

def activity_new(request):
    form = ActivityForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    return render(request, 'activities/activity_form.html', {'form': form, 'title': 'New Activity'})