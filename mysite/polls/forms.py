from django import forms
from review_upload.models import Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review', 'rating', 'date', 'sentiment')
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 1}),
        }

       