from .models import Comment, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)