from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                "placeholder": "potato",
                "class": "ClassName",
                "rows": 20,
                "cols": 120,
                "id": "myRandomID"
            }
        ))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("this is not a valid title")

    def clean_description(self, *args, **kwargs):
        email = self.cleaned_data.get("description")
        if not email.endswith("edu"):
            raise forms.ValidationError("THis is not a valid email")
        return  email

class RawProductForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}


    ))
    description = forms.CharField(
                        label='',
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "potato",
                                "class": "ClassName",
                                "rows": 20,
                                "cols": 120,
                                "id": "myRandomID"
                            }
                        ))
    price = forms.DecimalField(initial=199.99)
