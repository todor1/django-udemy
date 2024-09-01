from django import forms
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        # the second field is optional since the default value in the Model is False
        fields = ['item', 'completed']
