from django import forms
from .models import Produto

class cadProdForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'