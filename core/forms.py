from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, UserSkill, CareerGoal


class UserSkillForm(forms.ModelForm):

    class Meta:
        model = UserSkill

        fields = [
            'skill',
            'proficiency',
            'years_of_experience',
            'self_rating',
        ]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'full_name',
            'phone',
            'education',
            'college',
            'location',
            'bio',
            'profile_photo',
        ]

        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
        }


class CareerGoalForm(forms.ModelForm):

    class Meta:
        model = CareerGoal
        fields = [
            'target_role',
            'experience_level',
            'preferred_domain',
            'target_salary',
            'target_timeline',
        ]

        widgets = {
            'target_role': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Python Full Stack Developer'
                }
            ),

            'preferred_domain': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Web Development'
                }
            ),

            'target_salary': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g. 600000'
                }
            ),

            'target_timeline': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g. 6'
                }
            ),
        }
