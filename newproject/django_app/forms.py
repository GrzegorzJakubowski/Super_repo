from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',widget = forms.TextInput(attrs={"placeholder" : "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
            "placeholder": "Your description",
            "class": "new-class",
            "rows": 30,
            "cols": 150}))
    price = forms.DecimalField(initial=1.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")


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