from django.forms import ModelForm
from .models import File


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file']
