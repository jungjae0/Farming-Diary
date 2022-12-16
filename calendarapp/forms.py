from django.conf import settings
from django.forms import ModelForm, DateInput
from django.template.defaultfilters import filesizeformat

from calendarapp.models import Event, Item
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item']

        exclude = ["user"]

class EventForm(ModelForm):
    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     try:
    #         content_type = image.content_type.split('/')[0]
    #         if content_type in settings.CONTENT_TYPES:
    #             if image.size > int(settings.MAX_UPLOAD_SIZE):
    #                 raise forms.ValidationError(('Please keep filesize under %s. Current filesize %s') % (
    #                 filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(image.size)))
    #         else:
    #             raise forms.ValidationError('File type is not supported')
    #         return image
    #     except:
    #         return image

    class Meta:
        model = Event
        fields = ['title','start_time', 'end_time', 'item',
                  'description', 'active', 'image', 'level']

        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "내용을 입력하세요",
                }
            ),
            # "image": FileInput
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)