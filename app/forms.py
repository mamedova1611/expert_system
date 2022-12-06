from django.forms import ModelForm

from app.models import *

class OptionsForm(ModelForm):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = '__all__'