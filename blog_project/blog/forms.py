# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age']

    def clean_password2(self):
        # Validate that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','post_image']
       