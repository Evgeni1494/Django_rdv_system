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
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold',)
        
        widgets = {
            'name':forms.TextInput,
            'description':forms.Textarea,
            'price':forms.TextInput,
            'image':forms.FileInput,
            
        }









