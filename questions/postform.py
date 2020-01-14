from django import forms

class QuestionForm(forms.Form):
  title = forms.CharField(label="",min_length=300, max_length=300, widget=forms.TextInput(attrs={'size' : '100'}))
  content = forms.CharField(label="", widget=forms.Textarea(attrs={'id' : 'markdown'}))

class AnswerForm(forms.Form):
  content = forms.CharField(label="", widget=forms.Textarea(attrs={'id' : 'markdown'}))
