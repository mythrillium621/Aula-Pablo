from django.shortcuts import render
from .models import Item
from .forms import ItemForm
# from .models import Activity
# from .forms import ActivityForm


def lista(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    return render(request, "index.html", context)

def add_item(request): 
    if request.method == 'GET':
        form = ItemForm()
        context = {'form':form}
        return render(request, "add_item.html", context)
    
    from django.shortcuts import render, redirect


# def activity_list(request):
#     activities = Activity.objects.all()
#     return render(request, 'lista/activity_list.html', {'activities': activities})

# def activity_edit(request, id):
#     activity = Activity.objects.get(id=id)
#     form = ActivityForm(request.POST or None, instance=activity)
#     if form.is_valid():
#         form.save()
#         return redirect('activity_list')
#     return render(request, 'lista/activity_form.html', {'form': form, 'title': 'Edit Activity'})

# def activity_new(request):
#     form = ActivityForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('activity_list')
#     return render(request, 'lista/activity_form.html', {'form': form, 'title': 'New Activity'})