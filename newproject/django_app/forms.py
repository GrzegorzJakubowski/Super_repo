from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RowProductForm(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "placeholder" : "Your description",
            "class" : "new-class",
            "rows" : 30,
            "cols" : 150
        }
    ))
    price = forms.DecimalField(initial=1.99)