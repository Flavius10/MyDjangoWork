from django.forms import ModelForm
from django import forms
from .models import Project, Review 

class ProjectForm(ModelForm):
    """ Formular pentru creare/editare proiect. Include toate câmpurile și taguri multiple. """
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update({'class':'input'})

        # self.fields['description'].widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    """ Formular pentru adăugarea unui review (vot și comentariu). """
    class Meta:
        model = Review
        fields = ['value', 'body']

        label = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})