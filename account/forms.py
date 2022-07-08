from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']
        widgets = {
            'password': PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
