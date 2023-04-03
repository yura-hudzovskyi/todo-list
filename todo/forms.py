import datetime

from django import forms

from todo.models import Task, Tag


class DateInput(forms.DateInput):
    input_type = "date"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={"class": "scrollable-checkbox-list"}),
        queryset=Tag.objects.all(),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "completed"]
        widgets = {"deadline": DateInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({"class": "form-control"})
        self.fields["deadline"].widget.attrs.update({"class": "form-control"})

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline.date() < datetime.date.today():
            raise forms.ValidationError("Deadline cannot be in the past")
        return deadline
