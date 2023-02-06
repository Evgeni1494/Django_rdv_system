from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)
        
        widgets = {
            'category':forms.Select,
            'name':forms.TextInput,
            'description':forms.Textarea,
            'price':forms.TextInput,
            'image':forms.FileInput,
            
        }
        










