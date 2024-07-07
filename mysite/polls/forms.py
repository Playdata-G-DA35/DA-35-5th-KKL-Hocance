from django import forms
from . models import Post


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('id','title', 'contents','rating')
        widgets = {
            'rating': forms.NumberInput(attrs={'Min': 0, 'Max': 5, 'Step': 1}),
        }
       