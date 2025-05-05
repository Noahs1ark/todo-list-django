from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    fname = forms.CharField(max_length=100, required=True, label='First Name')
    lname = forms.CharField(max_length=100, required=True, label='Last Name')
    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['fname']  # Store the name in the User model's first_name field
        user.last_name = self.cleaned_data['lname']  # Store the name in the User model's last_name field
        if commit:
            user.save()
        return user

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['heading','description','due','category']
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter task description...','class': 'form-control'}),
            'due': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control','class': 'form-control'}) 
        }
        labels = {
            'heading': 'Task Title',
            'description': 'Task Description',
            'due': 'Due Date & time',
            'category': 'Category'
        }
        help_texts = {
            
        }
        error_messages = {
            'heading': {
                'max_length': 'The title is too long. Please keep it under 200 characters.',
            },
        }