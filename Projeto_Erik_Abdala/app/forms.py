from django import forms
from .models import *

class SubareaForm(forms.ModelForm):

    class Meta:

        model = Subarea

        fields = '__all__'

class TopicoForm(forms.ModelForm):

    class Meta:

        model = Topico

        fields = '__all__'