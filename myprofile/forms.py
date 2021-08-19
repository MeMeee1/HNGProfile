from django import forms
from .models import New

class PostForm(forms.ModelForm):
	class Meta:
		model = New
		fields = "__all__"
		widgets = {
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.TextInput(attrs={'class':'form-control form-sm'}),
		'comment':forms.Textarea(attrs={'class':'form-control form-sm'})
		}