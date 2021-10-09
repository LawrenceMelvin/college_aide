from django import forms
PERSON = [('student','Student'),('developer','Developer')]
WANTED = [('placement','Placement'),('job','Job'),('skill','Skill'),('english','English')]
class awareform(forms.Form):
    person = forms.ChoiceField(choices=PERSON)
    wanted = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=WANTED)
