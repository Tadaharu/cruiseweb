from django import forms
from cruiseWeb.models import Tweet, ObtainedDataNER


class NewNerForm(forms.ModelForm):

    class Meta():
        model = ObtainedDataNER
        fields = ['tLocation','tState']
        widgets = {
            'tLocation': forms.TextInput(attrs={'class': 'form-control'}),
            'tState': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            "tLocation": "Location List",
            "tState": "State List"
        }

    # def __init__ (self, text, *args, **kwargs):
    #     self.text = text
    #     super (NewNerForm, self).__init__ (*args, **kwargs)

    # def __init__ (self, tweet, *args, **kwargs):
    #     self.tweet = tweet
    #     super (NewNerForm, self).__init__ (*args, **kwargs)

    # location = forms.CharField(widget=forms.Textarea)
    # state = forms.CharField()

# class testForm(forms.ModelForm):
#     class Meta():
#         model = Tweet
#         fields = ['completed']
#         widgets = {'completed': forms.HiddenInput()}
