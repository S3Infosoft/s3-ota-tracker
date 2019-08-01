from django import forms


class TrackerForm(forms.Form):

    CHOICES = (
        (1, "Booking"),
        (2, "Goibibo"),
        (3, "MMT")
    )

    search = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control",
                                 "placeholder": "Search"
                             }))
    hotel = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                                "class": "form-control",
                                "placeholder": "Hotel"
                            }))
    ota = forms.ChoiceField(choices=CHOICES,
                            widget=forms.Select(attrs={
                                "class": "form-control"
                            }))
    check_in = forms.DateField(widget=forms.DateInput(attrs={
        "class": "form-control",
        "type": "date"
    }))

    check_out = forms.DateField(widget=forms.DateInput(attrs={
        "class": "form-control",
        "type": "date",
    }))
