from django import forms
from .models import Blogpost

class PostForm(forms.ModelForm):
	class Meta:
		model = Blogpost
		fields = ['title', 'category', 'image', 'content', 'summary', 'status']

