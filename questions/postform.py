from django import forms

class QuestionForm(forms.Form):
  title = forms.CharField(label="",max_length=140, widget=forms.TextInput(attrs={'class' : 'post-title'}))
  content = forms.CharField(label="", widget=forms.Textarea(attrs={'id' : 'markdown'}))

class AnswerForm(forms.Form):
  content = forms.CharField(label="", widget=forms.Textarea(attrs={'id' : 'markdown'}))
