from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Partner


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ['logo', 'about']
        labels = {
            'name': _('Partner name')
        }