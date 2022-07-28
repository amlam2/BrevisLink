from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from .models import Urlentry, Leads


class UrlentryForm(ModelForm):
    class Meta:
        model = Urlentry
        fields = ['full_url', 'owner']
    def __init__(self, *args, **kwargs):
        hide_condition = kwargs.pop('hide_condition', None)
        super(UrlentryForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['owner'].widget = HiddenInput()


class UrlentryFormShort(ModelForm):
    class Meta:
        model = Urlentry
        fields = ['full_url']
    def __init__(self, *args, **kwargs):
        super(UrlentryFormShort, self).__init__(*args, **kwargs)
        self.fields['full_url'].widget = HiddenInput()


class LeadsForm(ModelForm):
    class Meta:
        model = Leads
        fields = ['clicked_host']
