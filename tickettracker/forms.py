from django import forms

from .models import Ticket, TicketLogEntry


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'tags',]


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['severity', 'milestone', 'state',]


class LogEntryForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea, required=False, label='')

    def clean_body(self):
        value = self.cleaned_data.get('body', '').strip()
        if value == '':
            raise forms.ValidationError("Empty comment.")
        return value
