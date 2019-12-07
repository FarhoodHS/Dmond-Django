from django import forms
from django.core.exceptions import ValidationError

from shop.models import Member


class SignInForm(forms.ModelForm):

    class Meta:
        model = Member
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password']
    
    def _get_validation_exclusions(self):
        exclude = ['username']
        for f in self.instance._meta.fields:
            field = f.name
            if field not in self.fields:
                exclude.append(f.name)

            elif self._meta.fields and field not in self._meta.fields:
                exclude.append(f.name)
            elif self._meta.exclude and field in self._meta.exclude:
                exclude.append(f.name)

            elif field in self._errors:
                exclude.append(f.name)

            else:
                form_field = self.fields[field]
                field_value = self.cleaned_data.get(field)
                if not f.blank and not form_field.required and field_value in form_field.empty_values:
                    exclude.append(f.name)
        return exclude


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ['username', 'email', 'image', 'password', 'image']

    def clean_password1(self):
        raise ValidationError('x')

    def clean(self):
        raise self.add_error()
