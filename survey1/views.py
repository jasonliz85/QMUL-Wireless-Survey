
# Create your views here.

from django.contrib.auth            import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from django.template import Context, RequestContext, Template

from django.shortcuts import render_to_response

from django import forms

from models import Survey1

fivepoints = (
              ('5', "Excellent"),
              ('4', "Good"),
              ('3', "Average"),
              ('2', "Poor"),
              ('1', "Very Bad"),
              ('0', "No Comment"),
             )

class SurveyForm(forms.Form):
#class SurveyForm(forms.ModelForm):
#   class Meta:
#       model = Survey1
#       exclude = ('user', 'stamp')

    uses_wifi = forms.ChoiceField(widget=forms.RadioSelect, choices=(
                                  ('YES'     , "Yes"),
                                  ('NONEED'  , "Don't need it"),
                                  ('CANT'    , "Can't make it work"),
                                  ('COVERAGE', "Can't get a good signal"),
                                 ))
    coverage  = forms.ChoiceField(widget=forms.RadioSelect, choices=fivepoints)
    speed     = forms.ChoiceField(widget=forms.RadioSelect, choices=fivepoints)
    where     = forms.CharField(widget=forms.Textarea, required=False)
    whereelse = forms.CharField(widget=forms.Textarea, required=False)
    what      = forms.ChoiceField(widget=forms.RadioSelect, choices=(
                                  ('LAPTOP', "Laptop"),
                                  ('WINCE' , "Windows PDA"),
                                  ('IPOD'  , "Apple iPOD"),
                                  ('PDA'   , "Other PDA"),
                                  ('IPHONE', "Apple iPHONE"),
                                  ('BERRY' , "Blackberry"),
                                  ('PHONE' , "Other Mobile Phone"),
                                  ('NONE'  , "Not Applicable"),
                                 ))
    whos      = forms.ChoiceField(widget=forms.RadioSelect, choices=(
                                  ('DEPT' , "Department/Institute"),
                                  ('GRANT', "Grant suplied"),
                                  ('WORK' , "Other work supplied"),
                                  ('OWN'  , "My own"),
                                  ('NONE' , "Not Applicable"),
                                 ))
    admins    = forms.ChoiceField(widget=forms.RadioSelect, choices=(
                                 ('ITS'  , "IT Support"),
                                 ('DEPT' , "Department/Institute"),
                                 ('GROUP', "Group IT support"),
                                 ('WORK' , "Other work supplied"),
                                 ('ME'   , "I do it myself"),
                                 ('NONE' , "Not Applicable"),
                                ))
    comments  = forms.CharField(widget=forms.Textarea, required=False)

@login_required
def index_view(request):
    if request.method == 'POST':
        form=SurveyForm(request.POST)
        if form.is_valid():
            answer = Survey1(user     =request.user,
                             uses_wifi=form.cleaned_data['uses_wifi'],
                             coverage =form.cleaned_data['coverage'],
                             speed    =form.cleaned_data['speed'],
                             where    =form.cleaned_data['where'],
                             whereelse=form.cleaned_data['whereelse'],
                             what     =form.cleaned_data['what'],
                             whos     =form.cleaned_data['whos'],
                             admins   =form.cleaned_data['admins'],
                             comments =form.cleaned_data['comments'],
                            )
            answer.save()
            return render_to_response('survey1/index.html', {'form': form, })
    else:
        form = SurveyForm()
    return render_to_response('survey1/index.html', {'form': form})

