
""" Guideline content types.

"""

from five import grok

from zope import schema
from zope.component import adapts

from zope.interface import alsoProvides

from zope.app.container.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from z3c.form.interfaces import IEditForm
from z3c.form.interfaces import IAddForm
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.formwidget.contenttree.widget import MultiContentTreeWidget

from plone.directives import dexterity, form

from z3c.relationfield.schema import RelationChoice, RelationList

from plone.formwidget.contenttree import (
    ContentTreeFieldWidget,
    PathSourceBinder,
    ObjPathSourceBinder,
    )

import shmkbase.vocabularies as vocab

from shmkbase.guideline import config as guideline_config

from shmkbase.guideline import messageFactory as _


CUTOFF_CONTENT_TYPE = 'shmresearch.cutoffitem'

CUTOFF_SOURCE = ObjPathSourceBinder(portal_type = CUTOFF_CONTENT_TYPE)

FIELDS = guideline_config.GUIDELINE_FIELDS
GROUPS = guideline_config.GUIDELINE_FIELD_GROUPS


def getRecommendationField(name):
    return RelationList(
        title=_(name),
        default=[],
        value_type=RelationChoice(title=name,
                                  source=CUTOFF_SOURCE),
        required=False,
        )
        

## Guideline Container

class IGuidelineContainer(form.Schema):

    """ A guideline container.
    """


## Guideline

# GRADE/STRENGHT of RECOMMENDATION & QUALITY/LEVEL of EVIDENCE

class IGuidelineGrade(form.Schema):

    """ Guideline GRADE/STRENGHT of RECOMMENDATION & QUALITY/LEVEL of EVIDENCE schema.
    """

    # Fieldset
    form.fieldset(
        'grade_evidence_level',
        label=_(FIELDS['grade_evidence_level'][0]),
        fields=FIELDS['grade_evidence_level'][1],
        )

    grade_evidence_level = getRecommendationField(u'grade_evidence_level')
                    

# EPIDEMIOLOGY & STATISTICS |MECHANISMS OF THE DISEASE

class IGuidelineEpidemiology(form.Schema):

    """ Guideline Epidemiology schema.
    """

    # Fieldset
    form.fieldset(
        'epidemiology',
        label=_(FIELDS['epidemio'][0]),
        fields=FIELDS['epidemio'][1],
        )

    disease_incidence = getRecommendationField(u'disease_incidence')

    disease_mortality = getRecommendationField(u'disease_mortality')

    disease_prevalence = getRecommendationField(u'disease_prevalence')

    risk_of_being_diagnosed = getRecommendationField(u'risk_of_being_diagnosed in 10, 20, 30 years')

    risk_of_dying = getRecommendationField(u'risk_of_dying in 10, 20, 30 years')

    lifetime_risk_of_being_diagnosed = getRecommendationField(u'lifetime_risk_of_being_diagnosed')

    lifetime_risk_of_dying = getRecommendationField(u'lifetime_risk_of_dying')
    
    age_at_diagnosis = getRecommendationField(u'age_at_diagnosis')

    age_at_death = getRecommendationField(u'age_at_death')

    survival_rate = getRecommendationField(u'survival_rate (1, 3, 5, 10 years)')
    
    median_survival_times = getRecommendationField(u'median_survival_times (average survival times for people diagnosed)')


class IGuidelineDiseaseMechanisms(form.Schema):

    """ Guideline Disease Mechanisms schema.
    """
    
    # Fieldset
    form.fieldset(
        'disease_mechanisms',
        label=_(FIELDS['disease_mechanisms'][0]),
        fields=FIELDS['disease_mechanisms'][1],
        )
         
    form.widget(disease_attributes = CheckBoxFieldWidget)
    disease_attributes = schema.List(
        title = _(u"disease_attributes"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary = vocab.DISEASE_ATTRIBUTES),
        required = False, #True,
        )

    physiopathology_or_pathologic_processes = getRecommendationField(u'physiopathology_or_pathologic_processes')

    complications = getRecommendationField(u'complications')

                        
# SIGNS & SYMTOMS -> SymptomsAndTreatmentEditForm

class IGuidelineSymptoms(form.Schema):

    """ Guideline Signs & Symptoms schema.
    """

    # Fieldset
    form.fieldset(
        'symptoms',
        label=_(FIELDS['symptoms'][0]),
        fields=FIELDS['symptoms'][1],
        )

    #form.omitted(IAddForm, 'signs_and_symptoms')
    form.omitted('signs_and_symptoms')
    signs_and_symptoms = getRecommendationField(u'signs_and_symptoms')
    

# DIAGNOSIS & PRONOSIS -> SymptomsAndTreatmentEditForm

class IGuidelineDiagnosisAndPrognosis(form.Schema):

    """ Guideline Diagnosis & Prognosis schema.
    """

    # Fieldset
    form.fieldset(
        'diagnosis_and_prognosis',
        label=_(FIELDS['diagnosis_and_prognosis'][0]),
        fields=FIELDS['diagnosis_and_prognosis'][1],
        )

    form.omitted('diagnosis_physical_examination')
    diagnosis_physical_examination = getRecommendationField(u'diagnosis_physical_examination')



#                          'diagnostic_techniques_clinical_laboratory',
#                          'diagnostic_techniques_imaging',
#                          'diagnostic_techniques_cardiovascular',
#                          'diagnostic_techniques_digestive_system',
#                          'diagnostic_techniques_endocrine',
#                          'diagnostic_techniques_obstetrical_and_gynecological',
#                          'diagnostic_techniques_ophtalmological',
#                          'diagnostic_techniques_radioisotope',
#                          'diagnostic_techniques_respiratory_system',
#                          'diagnostic_techniques_surgical',
#                          'diagnostic_techniques_urological',
#                          'diagnostic_techniques_monitoring_physiologic',
#                          'diagnostic_techniques_self_evaluation',
#                          

    form.omitted('clinical_classification')
    clinical_classification = getRecommendationField(u'clinical_classification')

    form.omitted('diagnostic_algorithm')
    diagnostic_algorithm = getRecommendationField(u'diagnostic_algorithm')

    form.omitted('differential_diagnosis')
    differential_diagnosis = getRecommendationField(u'differential_diagnosis')

    form.omitted('prognosis_cure')
    prognosis_cure = getRecommendationField(u'prognosis_cure')

    form.omitted('prognosis_survival')
    prognosis_survival = getRecommendationField(u'prognosis_survival')

    form.omitted('prognosis_recurrence')
    prognosis_recurrence = getRecommendationField(u'prognosis_recurrence')
    
    form.omitted('prognosis_remission')
    prognosis_remission = getRecommendationField(u'prognosis_remission')
    
    form.omitted('prognosis_treatment_outcome')
    prognosis_treatment_outcome = getRecommendationField(u'prognosis_treatment_outcome')


# TREATMENT -> SymptomsAndTreatmentEditForm

class IGuidelineTreatment(form.Schema):

    """ Guideline Treatment schema.
    """

    # Fieldset
    form.fieldset(
        'treatment',
        label=_(FIELDS['treatment'][0]),
        fields=FIELDS['treatment'][1],
        )

    form.omitted('treatment_goals')
    treatment_goals = getRecommendationField(u'treatment_goals')

    form.omitted('treatment_strategies')
    treatment_strategies = getRecommendationField(u'treatment_strategies')

    form.omitted('drug_pharma_therapy_administration_and_dosage')
    drug_pharma_therapy_administration_and_dosage = getRecommendationField(u'drug_pharma_therapy_administration_and_dosage')

    form.omitted('drug_pharma_therapy_adverse_effects')
    drug_pharma_therapy_adverse_effects = getRecommendationField(u'drug_pharma_therapy_adverse_effects')
    
    form.omitted('drug_pharma_therapy_contraindications')
    drug_pharma_therapy_contraindications = getRecommendationField(u'drug_pharma_therapy_contraindications')
    
    form.omitted('drug_pharma_therapy_drug_interactions')
    drug_pharma_therapy_drug_interactions = getRecommendationField(u'drug_pharma_therapy_drug_interactions')

    form.omitted('nursing')
    nursing = getRecommendationField(u'nursing')

    form.omitted('prevention_and_control')
    prevention_and_control = getRecommendationField(u'prevention_and_control')

    form.omitted('radiotherapy')
    radiotherapy = getRecommendationField(u'radiotherapy')

    form.omitted('rehabilitation')
    rehabilitation = getRecommendationField(u'rehabilitation')

    form.omitted('surgery')
    surgery = getRecommendationField(u'surgery')

    form.omitted('dietary_supplements')
    dietary_supplements = getRecommendationField(u'dietary_supplements')

    form.omitted('lifestyle_changes_smoking')
    lifestyle_changes_smoking = getRecommendationField(u'lifestyle_changes_smoking')

    form.omitted('lifestyle_changes_alcohol')
    lifestyle_changes_alcohol = getRecommendationField(u'lifestyle_changes_alcohol')

    form.omitted('lifestyle_changes_weight')
    lifestyle_changes_weight = getRecommendationField(u'lifestyle_changes_weight')

    form.omitted('lifestyle_changes_diet')
    lifestyle_changes_diet = getRecommendationField(u'lifestyle_changes_diet')

    form.omitted('lifestyle_changes_physical_exercise')
    lifestyle_changes_physical_exercise = getRecommendationField(u'lifestyle_changes_physical_exercise')

    form.omitted('lifestyle_changes_stress')
    lifestyle_changes_stress = getRecommendationField(u'lifestyle_changes_stress')

    form.omitted('lifestyle_changes_sleep')
    lifestyle_changes_sleep = getRecommendationField(u'lifestyle_changes_sleep')

    form.omitted('treatment_algorithm')
    treatment_algorithm = getRecommendationField(u'treatment_algorithm')


# PATIENT FOLLOW-UP

class IGuidelinePatientFollowUp(form.Schema):

    """ Guideline Patient Follow-Up schema.
    """

    # Fieldset
    form.fieldset(
        'patient_followup',
        label=_(FIELDS['patient_followup'][0]),
        fields=FIELDS['patient_followup'][1],
        )

    form.omitted('patient_followup')
    patient_followup = getRecommendationField(u'patient_followup')


# RISK ASSESSMENT

class IGuidelineRiskAssessment(form.Schema):

    """ Guideline Risk Assessment schema.
    """
    
    # Fieldset
    form.fieldset(
        'riskassessment',
        label=_(FIELDS['riskassessment'][0]),
        fields=FIELDS['riskassessment'][1],
        )

    form.omitted('risk_factors_age')
    risk_factors_age = getRecommendationField(u'risk_factors_age')

    form.omitted('risk_factors_family_history')
    risk_factors_family_history = getRecommendationField(u'risk_factors_family_history')

    form.omitted('risk_factors_personal_history')
    risk_factors_personal_history = getRecommendationField(u'risk_factors_personal_history')
                    
    form.omitted('risk_factors_genetic_or_genomic')
    risk_factors_genetic_or_genomic = getRecommendationField(u'risk_factors_genetic_or_genomic')
	
    form.omitted('risk_factors_smoking_habits')
    risk_factors_smoking_habits = getRecommendationField(u'risk_factors_smoking_habits')
	
    form.omitted('risk_factors_alcohol_consumption')
    risk_factors_alcohol_consumption = getRecommendationField(u'risk_factors_alcohol_consumption')
	
    form.omitted('risk_factors_dietary_habits')
    risk_factors_dietary_habits = getRecommendationField(u'risk_factors_dietary_habits')
	
    form.omitted('risk_factors_amount_of_physical_exercise')
    risk_factors_amount_of_physical_exercise = getRecommendationField(u'risk_factors_amount_of_physical_exercise')
	
    form.omitted('risk_factors_obesity_or_overweight')
    risk_factors_obesity_or_overweight = getRecommendationField(u'risk_factors_obesity_or_overweight')
	
    form.omitted('risk_factors_sleep_habits_or_disorders')
    risk_factors_sleep_habits_or_disorders = getRecommendationField(u'risk_factors_sleep_habits_or_disorders')

    form.omitted('risk_factors_stress')
    risk_factors_stress = getRecommendationField(u'risk_factors_stress')
	
    form.omitted('risk_factors_drug_or_substance_intake')
    risk_factors_drug_or_substance_intake = getRecommendationField(u'risk_factors_drug_or_substance_intake')
	
    form.omitted('risk_factors_disease')
    risk_factors_disease = getRecommendationField(u'risk_factors_disease')
	
    form.omitted('risk_factors_infectious_agents')
    risk_factors_infectious_agents = getRecommendationField(u'risk_factors_infectious_agents')
	
    form.omitted('risk_markers')
    risk_markers = getRecommendationField(u'risk_markers')
	
    form.omitted('risk_stratification')
    risk_stratification = getRecommendationField(u'risk_stratification')



# SCREENING

class IGuidelineScreening(form.Schema):

    """ Guideline Screening schema.
    """

    # Fieldset
    form.fieldset(
        'screening',
        label=_(FIELDS['screening'][0]),
        fields=FIELDS['screening'][1],
        )

    form.omitted('screening_goals')
    screening_goals = getRecommendationField(u'screening_goals')
    
    form.omitted('screening_tests')
    screening_tests = getRecommendationField(u'screening_tests')
    
    form.omitted('starting_age')
    starting_age = getRecommendationField(u'starting_age')
    
    form.omitted('stopping_age')
    stopping_age = getRecommendationField(u'stopping_age')
    
    form.omitted('screening_intervals')
    screening_intervals = getRecommendationField(u'screening_intervals')
    
    form.omitted('screening_cutpoint_or_cutoff')
    screening_cutpoint_or_cutoff = getRecommendationField(u'screening_cutpoint_or_cutoff')
    
    form.omitted('screening_algorithm')
    screening_algorithm = getRecommendationField(u'screening_algorithm')
    
    form.omitted('confirmatory_diagnostic_tests')
    confirmatory_diagnostic_tests = getRecommendationField(u'confirmatory_diagnostic_tests')
    
    form.omitted('benefits_of_screening')
    benefits_of_screening = getRecommendationField(u'benefits_of_screening')
    
    form.omitted('harms_of_screening')
    harms_of_screening = getRecommendationField(u'harms_of_screening')
    
    form.omitted('statistics_participation_rate_for_screening')
    statistics_participation_rate_for_screening = getRecommendationField(u'statistics_participation_rate_for_screening')

    form.omitted('statistics_persons_screened')
    statistics_persons_screened = getRecommendationField(u'statistics_persons_screened')




## GUIDELINE
class IGuideline(
                 IGuidelinePatientFollowUp,
                 IGuidelineTreatment,
                 IGuidelineDiagnosisAndPrognosis,
                 IGuidelineSymptoms,
                 IGuidelineScreening,
                 IGuidelineRiskAssessment,
                 IGuidelineDiseaseMechanisms,
                 IGuidelineEpidemiology,
                 IGuidelineGrade,
                 ):

    """ A guideline.
    """

    # categorization fieldset
#     form.fieldset(
#         'categorization',
#         label=_(u'Categorization'),
#         fields=['categories',],
#         )

#     form.widget(categories = CheckBoxFieldWidget)
#     categories = schema.List(
#         title = _(u"Categories"),
#         value_type = schema.Choice(
#          #  title = _(u"Selection"),
#             vocabulary = vocab.GUIDELINE_CATEGORIES),
#         required = False, #True,
#         )

    definitions = RelationList(
        title=_(u'definitions'),
        default=[],
        value_type=RelationChoice(title=u'definitions',
                               source=ObjPathSourceBinder(portal_type = 'shmresearch.definitionitem')),
        required=False,
        )

    prevention = getRecommendationField(u'prevention')



###########################################################################

    
    
class View(dexterity.DisplayForm):
    grok.context(IGuideline)
    grok.require('zope2.View')

    def getFieldsWithoutCutoffs(self):
        return ['disease_attributes',]

    def getCutoffObjs(self, attr):
        objs = []
        rels = getattr(self.context, attr, [])
        for rel in rels:
            #print rel
            #print rel.to_object
            obj = rel.to_object
            if obj is not None:  # we make sure the referenced object has not been deleted !
                objs.append(obj)
        return objs

    def getCutoffItems(self, attr):
        items = []
        rels = getattr(self.context, attr, [])
        for rel in rels:
            #print rel
            #print rel.to_object
            obj = rel.to_object
            if obj is not None:  # we make sure the referenced object has not been deleted !
                title = obj.Title()
                url = obj.absolute_url()
                text = obj.text
                #text = text.output
                item = {'title': title,
                        'url': url,
                        'text': text}
                items.append(item)
        return items
    
    def getFieldGroups(self):
        return GROUPS
    
    def getFieldnamesByGroup(self, group):
        return FIELDS.get(group)[1]
        
        
