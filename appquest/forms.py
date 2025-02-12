from django import forms


class QuestionForm(forms.Form):

    questao = forms.CharField()

