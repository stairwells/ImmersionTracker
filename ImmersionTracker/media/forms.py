from django.forms import ModelForm, TextInput
from ImmersionTracker.media.models import ReadingMedia, ListeningMedia


class BaseMediaForm(ModelForm):
    class Meta:
        abstract = True
        widgets = {
            'type': TextInput(attrs={
                'placeholder': 'Genre, physical or digital, etc.',
            }),
            'link': TextInput(attrs={
                'placeholder': 'Link to an external resource (e.g. a database)'
            }),
        }
        fields = ('name', 'type', 'link', 'status',)


class ReadingMediaForm(BaseMediaForm):
    class Meta(BaseMediaForm.Meta):
        model = ReadingMedia


class ListeningMediaForm(BaseMediaForm):
    class Meta(BaseMediaForm.Meta):
        model = ListeningMedia

