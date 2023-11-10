#Import of models
from django import forms
from .models import bestia

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

#Creation of form for register
class Newbestia(forms.ModelForm):
    class Meta:
        model = bestia
        fields = ("name", "descripcion", "cultura", "image",)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'descripcion': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'cultura': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'img': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
#Form for edit 
        
class Editbestia(forms.ModelForm):
    class Meta:
        model = bestia
        fields = ("name", "descripcion", "cultura", "image")
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'descripcion': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'cultura': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'img': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
    
    