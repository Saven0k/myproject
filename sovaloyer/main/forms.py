from django import forms
import datetime
from .models import Author
class GameTypeForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('C', 'coins'), ('D', 'dice'), ('N','number')])
    throws_number = forms.IntegerField(min_value=1, max_value=64)
    
    
# class AuthorAddForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=50)
#     bio = forms.CharField(max_length=300)
#     bithday = forms.DateField(initial=datetime.date.today)

class AuthorAddForm (forms.ModelForm):
    class Meta:
        model=Author
        fields = ['name', 'last_name', 'email', 'bio', 'bithday']
        
        
class ArticleAddForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите название статьи'}))
    content = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Текст статьи'}))
    date_of_published = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    is_published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    category = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите категорию статьи'}))
    