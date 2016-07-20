"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import NumericTraits, Species, OtherTraits
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

        LastVal = NumericTraits.objects.all().order_by('-feature_id').values_list()[0][0] + 1
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = 'dbPost'
  
        self.helper.layout = Layout(

            Div(                    
                HTML('<div id="div_id_species" class="control-group"> <label id="specieslab" for="id_species" class="control-label requiredField">\
                Species<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" data-live-search="true" name="species" id="id_species">\
                <option>Select by scientific name</option>{% for x in species %}<option value={{x.species_id_html}}>{{x.species_id}}</option>{% endfor %}</select></div> </div>'),

                #Field('species__genus_species', css_class='selectpicker show-tick', data_live_search="true", name="specSearch", id="specSearch"),
                style = 'width:50%; display:inline-block;',                            
                ),
            Div(
                HTML("<a href='/EntryKey' target='_blank' class='btn btn-warning'><span class='glyphicon glyphicon-list-alt'></span> Data Entry Key </a>"),
                style = "float:right;"
                ),
            HTML("<hr />"),            
            
            Fieldset('Add Trait',                       
                       Div(
                           HTML('<div id="div_id_traits" class="control-group"> <label id="traitlab" for="id_traits" class="control-label requiredField">\
                Numeric Traits<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" name="traits" id="id_traits">\
                <option>Select trait to add</option>{% for x in numtraits %}<option value="{{x.traits}}">{{x.traits}}</option>{% endfor %}</select></div> </div>'),
                           
                           HTML('<div id="div_id_units" class="control-group"> <label id="unitlab" for="id_units" class="control-label requiredField">\
                Units<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" name="units" id="id_units">\
                <option>Select units</option>{% for x in units %}<option value="{{x.units}}">{{x.units}}</option>{% endfor %}</select></div> </div>'),
                           
                           HTML('<div id="div_id_uncertainty" class="control-group"> <label id="uncertaintylab" for="id_uncertainty" class="control-label requiredField">\
                Uncertainty <span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" name="uncertainty" id="id_uncertainty">\
                <option>Select uncertainty</option><option value="ex">Exact</option><option value="ca">Approximate</option><option value="+">Greater than</option>\
                <option value="-">Less than</option></select></div> </div>'),
                           css_class='col-md-3 input-md'
                           ),

                       Div('mean',
                           HTML('<h4> And/or </h4>'),
                           HTML(
                           ' <div id="div_id_range" class="control-group"> <label for="id_range_0" class="control-label ">Range\
                            </label> <div class="controls"> <input class="numberinput" id="id_range_0" name="range_0" type="number">\
                            <span> Lower</span><input class="numberinput" id="id_range_1" name="range_1" type="number"><span>  Upper</span> </div> </div>'                         
                           ),
                           css_class = 'col-md-3 input-md',                           
                           ),
                       Div(
                           HTML('<div id="div_id_citation" class="control-group"> <label id="citationlab" for="id_citation" class="control-label requiredField">\
                Citation <span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" data-live-search="true" name="citation" id="id_citation">\
                <option>Select citation</option>{% for x in citations %}<option value="{{x.citation_name}}">{{x.citation_name}}</option>{% endfor %}</select></div> </div>'
                            ),
                           HTML('<div class="col-md-12"><br /></div>'),
                           HTML('<a href="/admin/app/citation/add/" target="_blank" class="btn btn-danger"> Add new citation </a>'),
                           css_class='col-md-3 input-md'
                           ),                                             
                       Div('comments',
                           css_class = 'col-md-3 input-md'
                           ),
                       HTML('<div class="col-md-5"><br /></div>'),
                       


                     ),
                HTML("<br />"),
                                               
                Fieldset('Save the data',

                       HTML('<div id="div_id_feature_id" style="display:none" class="col-md-3 control-group"> <label for="id_feature_id" class="control-label requiredField">\
                Feature id<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="numberinput" id="id_feature_id" name="feature_id" type="number" value="'+str(LastVal)+'"> </div> </div>'),
                       HTML('<div id="div_id_username" style="display:none" class="col-md-3 control-group"> <label for="id_username" class="control-label requiredField">\
                Username<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="textinput textInput" id="id_username" maxlength="30" name="username" type="text" value={{user.username}}> </div> </div>'),                                     
                       HTML('<div id="div_id_dt" style="display:none" class="col-md-3 control-group"> <label for="id_dt" class="control-label requiredField">\
                Dt<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="textinput textInput" id="id_dt" maxlength="30" name="dt" type="text" value={{day}}/{{month}}/{{year}}> </div> </div>'),                                        
                       Div(
                           FormActions(Submit('dbPost', 'Save data', css_class='btn btn-success',action=".")),
                           css_class = 'col-md-3'
                           ),
                       HTML('<div class="col-md-3" id="savesuccess"></div>')
                        ),
                        
                )


    class Meta:
        model = NumericTraits
        fields = ('mean','comments')
 
class PostFormOther(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostFormOther, self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].error_messages = {'required': 'This field is required'}

        LastVal = OtherTraits.objects.all().order_by('-trt_id').values_list()[0][0] + 1
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = 'dbPostother'
        self.helper.form_id = 'dbPostother_id'
  
        self.helper.layout = Layout(

            Div(                    
                HTML('<div id="div_id_species" class="control-group"> <label id="specieslab" for="id_species" class="control-label requiredField">\
                Species<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" data-live-search="true" name="species" id="id_species">\
                <option>Select by scientific name</option>{% for x in species %}<option value={{x.species_id_html}}>{{x.species_id}}</option>{% endfor %}</select></div> </div>\
                <div id="specieserror"></div>'),
              
                style = 'width:50%; display:inline-block;',                            
                ),
            Div(
                HTML("<a href='/EntryKey' target='_blank' class='btn btn-warning'><span class='glyphicon glyphicon-list-alt'></span> Data Entry Key </a>"),
                style = "float:right;"
                ),
            HTML("<hr />"),            
            
            Fieldset('Add Trait',                       
                       Div(
                           HTML('<div id="div_id_traits" class="control-group"> <label for="id_traits" class="control-label requiredField">\
                Character Traits<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" onchange="traitopts()" name="traits" id="id_traits">\
                {% for x in traits %}<option value="{{x.variable}}">{{x.variable}}</option>{% endfor %}</select></div> </div>'),                           
                           css_class='col-md-3 input-md'
                           ),

                       Div(
                           HTML('<div id="div_id_traitopt" class="control-group"> <label id="traitoptlab" for="id_traitopt" class="control-label requiredField">\
                Trait values<span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" name="traitopt" id="id_traitopt">\
                <option>Select value</option>{% for x in traitopts %}<option value="{{x.tr_value}}">{{x.tr_name}}</option>{% endfor %}</select></div> </div>'),                           
                           css_class = 'col-md-3 input-md',                           
                           ),
                       Div(
                           HTML('<div id="div_id_citation" class="control-group"> <label id="citationlab" for="id_citation" class="control-label requiredField">\
                Citation <span class="asteriskField">*</span> </label> <div class="controls"> <select class="selectpicker show-tick" data-live-search="true" name="citation" id="id_citation">\
                <option>Select citation</option>{% for x in citations %}<option value="{{x.citation_name}}">{{x.citation_name}}</option>{% endfor %}</select></div> </div>'
                            ),
                           HTML('<div class="col-md-12"><br /></div>'),
                           HTML('<a href="/admin/app/citation/add/" target="_blank" class="btn btn-danger"> Add new citation </a>'),
                           css_class='col-md-3 input-md'
                           ),                                             
                       Div('comments',
                           css_class = 'col-md-3 input-md'
                           ),
                       HTML('<div class="col-md-5"><br /></div>'),                       
                     ),
                HTML("<br />"),
                                               
                Fieldset('Save the data',

                       HTML('<div id="div_id_trtid" style="display:none" class="col-md-3 control-group"> <label for="id_trtid" class="control-label requiredField">\
                Feature id<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="numberinput" id="id_trtid" name="trtid" type="number" value="'+str(LastVal)+'"> </div> </div>'),
                       HTML('<div id="div_id_username" style="display:none" class="col-md-3 control-group"> <label for="id_username" class="control-label requiredField">\
                Username<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="textinput textInput" id="id_username" maxlength="30" name="username" type="text" value={{user.username}}> </div> </div>'),                                     
                       HTML('<div id="div_id_dt" style="display:none" class="col-md-3 control-group"> <label for="id_dt" class="control-label requiredField">\
                Dt<span class="asteriskField">*</span> </label> <div class="controls"> <input readonly class="textinput textInput" id="id_dt" maxlength="30" name="dt" type="text" value={{day}}/{{month}}/{{year}}> </div> </div>'),                                        
                       Div(
                           FormActions(Submit('dbPostother', 'Save data', css_class='btn btn-success', action=".")),
                           css_class = 'col-md-3'
                           ),
                       HTML('<div class="col-md-3" id="savesuccess"></div>'),                       
                        ),
                                                
                )


    class Meta:
        model = OtherTraits
        fields = ('comments',)        