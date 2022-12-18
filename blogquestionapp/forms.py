from .models import QuestionComment
from django import forms


class QuestionCommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        fields = ('content',)