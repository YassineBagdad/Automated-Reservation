from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import main.selenium_folder.functions as f1

# class CreateNewList(forms.Form):
#     name = forms.CharField(label="Name",max_length=200)
#     check = forms.BooleanField()

# class User(forms.Form):
#      username = forms.CharField(label='username', max_length=100)
#      password = forms.CharField(widget=forms.PasswordInput)

#class reservation(UserCreationForm):

class SettingsForm(forms.Form):
	listCountries = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	listcities = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	listBuildings = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	listFloors = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	
	Countries = forms.ChoiceField(choices=listCountries)
	cities = forms.ChoiceField(choices=listcities)
	Buildings = forms.ChoiceField(choices=listBuildings)
	Floors = forms.ChoiceField(choices=listFloors)

	#forms.TypedMultipleChoiceField( choices="tuple_of_tuples", coerce="coerce_function", empty_value=None)
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # message = forms.CharField(max_length=1000)



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "first_name","last_name","email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )