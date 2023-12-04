from django import forms
from lista.models import Item
#from .models import Activity

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

        from django import forms

# class ActivityForm(forms.ModelForm):
#     class Meta:
#         model = Activity
#         fields = ['name', 'time_spent']