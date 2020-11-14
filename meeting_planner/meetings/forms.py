from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput
from django.core.exceptions import ValidationError

from .models import Meeting


class NewMeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"}),
        }

        def set_future_date_only(self):
            set_date = self.cleaned_data.get("date")
            if set_date < date.today():
                raise ValidationError("Meetings cannot be added in the past")
            return set_date
