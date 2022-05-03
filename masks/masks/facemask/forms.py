from django import forms
from .models import MaskCreator, SupportModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MaskCreatorForm(forms.ModelForm):
  class Meta:
    model = MaskCreator
    fields = ('usuario','tela','color','capas')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class SupportForm(forms.ModelForm):
  #  comment = forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows': 20}))
    class Meta:
        model = SupportModel
        fields = "__all__"
        labels = {"asunto":"Asunto", "comment":"Comentario"}
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 80, 'rows': 10,'style':'resize:none;'}),
            'asunto' : forms.Textarea(attrs={'cols': 80, 'rows': 1,'style':'resize:none;'}),
        }
