from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="Description")
    text = forms.CharField(label="Articulo", widget=forms.Textarea(
            attrs={
                "placeholder": "Your Article",
                "class": "ClassName",
                "rows": 20,
                "cols": 120,
                "id": "myRandomID"
            }
        ))
    likes = forms.DecimalField(label="Likes", initial=0)
    featured = forms.BooleanField(initial=True)

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'text',
            'likes',
            'featured'

        ]


    '''
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    likes = models.DecimalField(max_digits=1000, decimal_places=3)
    text = models.TextField(default='patata')
    featured = models.BooleanField(default=False)
    '''