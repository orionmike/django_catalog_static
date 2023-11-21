
from django import forms
from .models import *

from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'slug': forms.TextInput(attrs={'class': 'uk-input'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # self.clean_data.get('slug')

        if new_slug == 'create':
            raise ValidationError('slug not be <create>')
        if Tag.objects.filter(slug=new_slug).count():
            raise ValidationError(f'slug {new_slug} already exist. slug must be unique')

        return new_slug


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'slug': forms.TextInput(attrs={'class': 'uk-input'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # self.clean_data.get('slug')

        if new_slug == 'create':
            raise ValidationError('slug not be <create>')
        if Category.objects.filter(slug=new_slug).count():
            raise ValidationError(f'slug {new_slug} already exist. slug must be unique')

        return new_slug


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'slug', 'preview_text', 'full_text', 'tag_list', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'slug': forms.TextInput(attrs={'class': 'uk-input'}),
            'preview_text': forms.Textarea(attrs={'class': 'uk-input'}),
            'full_text': forms.Textarea(attrs={'class': 'uk-input'}),
            'tag_list': forms.SelectMultiple(attrs={'class': 'uk-select'}),
            'category': forms.Select(attrs={'class': 'uk-select'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # self.clean_data.get('slug')

        if new_slug == 'create':
            raise ValidationError('slug not be <create>')
        # if Post.objects.filter(slug=new_slug).count():
        #     raise ValidationError(f'slug {new_slug} already exist. slug must be unique')

        return new_slug
