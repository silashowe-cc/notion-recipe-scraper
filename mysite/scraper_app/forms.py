from django import forms

class ScraperForm(forms.Form):
    token = forms.CharField(max_length=100)
    dbid = forms.CharField(max_length=100)
    recipe_url = forms.CharField(max_length=200)
    icon = forms.CharField(max_length=1)