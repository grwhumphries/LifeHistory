"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Traits, Species
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset, Field, Layout, HTML, ButtonHolder, MultiField
from crispy_forms.bootstrap import InlineCheckboxes, Div, FormActions, AccordionGroup, Accordion, Container, PrependedText, StrictButton



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class PostForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args,**kwargs)

        LastVal = Traits.objects.all().order_by('-feature_id').values_list()[0][0] + 1
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = 'dbPost'
  
        self.helper.layout = Layout(

            Div(                    
                HTML('<div id="div_id_species" class="control-group"> <label for="id_species" class="control-label requiredField">\
                Species<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" data-live-search="true" name="species" id="id_species">\
                <option>Select by scientific name</option>{% for x in species %}<option value={{x.species_id}}>{{x.genus_species}}</option>{% endfor %}</select></div> </div>'),

                #Field('species__genus_species', css_class='selectpicker show-tick', data_live_search="true", name="specSearch", id="specSearch"),
                style = 'width:50%; display:inline-block;',                            
                ),
            Div(
                HTML("<a href='/EntryKey' target='_blank' class='btn btn-warning'><span class='glyphicon glyphicon-list-alt'></span> Data Entry Key </a>"),
                style = "float:right;"
                ),
            HTML("<hr />"),            
            
            Fieldset('Size',                       
                       Div(
                           'female_mass_mean',
                           'female_mass_lower',
                           'female_mass_upper',
                           'female_mass_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                       Div(
                           'male_mass_mean',
                           'male_mass_lower',
                           'male_mass_upper',
                           'male_mass_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                       
                       Div(
                           'max_growth_mean',
                           'max_growth_lower',
                           'max_growth_upper',
                           'max_growth_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                  
                  
                       Div(
                           'wingspan_mean',
                           'wingspan_lower',
                           'wingspan_upper',
                           'wingspan_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                     ),
                HTML("<br />"),
                Fieldset('Age and Survival',                                    
                       Div(
                           'age_first_breed_mean',
                           'age_first_breed_lower',
                           'age_first_breed_upper',
                           'age_first_breed_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                       Div(
                           'max_age_mean',
                           'max_age_lower',
                           'max_age_upper',
                           'max_age_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                       
                       Div(
                           'annual_survival_mean',
                           'annual_survival_lower',
                           'annual_survival_upper',
                           'annual_survival_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                  
                     ),
                HTML("<br />"),
                Fieldset('Chick care',                                    
                       Div(
                           'clutch_size_mean',
                           'clutch_size_lower',
                           'clutch_size_upper',
                           'clutch_size_uncertainty',
                           'clutch_interval',
                           css_class = 'col-md-3 input-md'
                           ),
                       Div(
                           'incubation_mean',
                           'incubation_period_lower',
                           'incubation_period_upper',
                           'incubation_period_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                       
                       Div(
                           'fledging_period_mean',
                           'fledging_period_lower',
                           'fledging_period_upper',
                           'fledging_period_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),
                       
                       Div(
                           'post_fledge_care_mean',
                           'post_fledge_care_lower',
                           'post_fledge_care_upper',
                           'post_fledge_care_uncertainty',
                           css_class = 'col-md-3 input-md'
                           ),                 
                     ),
                HTML("<br />"),
                Fieldset('Other Fields',                                    
                       Div(
                           'foraging_distance',
                           'coloniality',
                           'mate_fidelity',
                           'site_fidelity',
                           css_class = 'col-md-3 input-md'
                           ),
                       Div(
                           'citation',
                           css_class = 'col-md-9 input-md'
                           ),
                                                                                                                                                                                                       
                       ),                                
                Fieldset('Save the data',

                       HTML('<div id="div_id_feature_id" class="col-md-3 control-group"> <label for="id_feature_id" class="control-label requiredField">\
                Feature id<span class="asteriskField">*</span> </label> <div class="controls"> <input class="numberinput" display="none" id="id_feature_id" name="feature_id" type="number" value="'+str(LastVal)+'"> </div> </div>'),
                       HTML('<div id="div_id_username" class="col-md-3 control-group"> <label for="id_username" class="control-label requiredField">\
                Username<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="textinput textInput" id="id_username" maxlength="30" name="username" type="text" value={{user.username}}> </div> </div>'),                                     
                       HTML('<div id="div_id_dt" class="col-md-3 control-group"> <label for="id_dt" class="control-label requiredField">\
                Dt<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="textinput textInput" id="id_dt" maxlength="30" name="dt" type="text" value={{day}}/{{month}}/{{year}}> </div> </div>'),                                        
                       Div(
                           FormActions(Submit('dbPost', 'Save data', css_class='btn btn-success')),
                           css_class = 'col-md-3'
                           )
                        )
                )


    class Meta:
        model = Traits
        fields = ('female_mass_mean','female_mass_mean', 'female_mass_upper', 'female_mass_lower', 'female_mass_uncertainty', 
                  'male_mass_mean', 'male_mass_lower', 'male_mass_upper', 'male_mass_uncertainty', 'clutch_size_mean', 'clutch_size_lower', 'clutch_size_upper', 
                  'clutch_size_uncertainty', 'clutch_interval', 'incubation_mean', 'incubation_period_lower', 'incubation_period_upper', 'incubation_period_uncertainty',
                  'fledging_period_mean', 'fledging_period_lower', 'fledging_period_upper', 'fledging_period_uncertainty', 'max_growth_mean', 'max_growth_lower', 'max_growth_upper',
                  'max_growth_uncertainty', 'post_fledge_care_mean', 'post_fledge_care_lower', 'post_fledge_care_upper', 'post_fledge_care_uncertainty', 'age_first_breed_mean', 'age_first_breed_lower',
                  'age_first_breed_upper', 'age_first_breed_uncertainty', 'foraging_distance', 'wingspan_mean', 'wingspan_lower', 'wingspan_upper', 'wingspan_uncertainty', 'max_age_mean', 'max_age_lower',
                  'max_age_upper', 'max_age_uncertainty', 'annual_survival_mean', 'annual_survival_lower', 'annual_survival_upper', 'annual_survival_uncertainty','coloniality','mate_fidelity','site_fidelity','citation')
