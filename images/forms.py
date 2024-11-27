
import requests
from django import forms
from django.utils.text import slugify

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']

        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extentions = ['jpg', 'jpeg', 'png']
        extension = url.split('.')[-1].lower()
        if extension not in valid_extentions:
            raise forms.ValidationError("Podany adres nie zawiera prawidlowego rozszerzenia")

        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extention = image_url.split('.')[-1].lower()
        image_names = f'{name}.{extention}'

        response = requests.get(image_url)
        image.image.save()

        if commit:
            image.save()
        return image