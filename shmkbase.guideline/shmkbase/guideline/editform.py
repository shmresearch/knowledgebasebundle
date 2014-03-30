from five import grok

from zope.interface import alsoProvides

from plone.directives import dexterity, form

from z3c.form.interfaces import IEditForm
#from z3c.form.interfaces import IDisplayForm

from shmkbase.guideline.content import (
                                  IGuideline,
                                  IGuidelineRiskAssessment,
                                  IGuidelineScreening,
                                  IGuidelinePatientFollowUp,
                                  IGuidelineTreatment,
                                  IGuidelineDiagnosisAndPrognosis,
                                  IGuidelineSymptoms,
                                  
                                  #View,
                                  )



###########################  Grouping schemas for specific Edit Forms  #######################################

class IRiskAssessmentAndScreening(IGuidelineRiskAssessment,
                                  IGuidelineScreening):

    """ Risk Assessment and Screening schema for the RiskAssessmentAndScreeningEditView form.
    """
    
    form.no_omit(IEditForm,   
    
                # Risk Assessment fields
                'risk_factors_age',
                         'risk_factors_family_history',
                         'risk_factors_personal_history',
						'risk_factors_genetic_or_genomic',
						'risk_factors_smoking_habits',
						'risk_factors_alcohol_consumption',
						'risk_factors_dietary_habits',
						'risk_factors_amount_of_physical_exercise',
						'risk_factors_obesity_or_overweight',
						'risk_factors_sleep_habits_or_disorders',
						'risk_factors_stress',
						'risk_factors_drug_or_substance_intake',
						'risk_factors_disease',
						'risk_factors_infectious_agents',
						'risk_markers',
						'risk_stratification',

                # Screening fields
                'screening_goals',
                         'screening_tests',
                         'starting_age',
                         'stopping_age',
                         'screening_intervals',
                         'screening_cutpoint_or_cutoff',
                         'screening_algorithm',
                         'confirmatory_diagnostic_tests',
                         'benefits_of_screening',
                         'harms_of_screening',
                         'statistics_participation_rate_for_screening',
                         'statistics_persons_screened',
                         
                )

    
# Schema used to provide fields to the SymptomsAndTreamentEditView form.
class ISymptomsAndTreatment(
                 IGuidelinePatientFollowUp,
                 IGuidelineTreatment,
                 IGuidelineDiagnosisAndPrognosis,
                 IGuidelineSymptoms
                 ):

    """ Symptoms and Treatment schema for the SymptomsAndTreamentEditView form.
    """
    
    #form.no_omit(View, 'signs_and_symptoms',) Specify an interface for the view, and use it instead !!!
    
    form.no_omit(IEditForm, 
    
                # Signs and Symptoms fields
                'signs_and_symptoms',
                
                # Diagnosis and Prognosis fields
                'diagnosis_physical_examination',
                         #'diagnostic_techniques_clinical_laboratory',
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
                         #'diagnostic_techniques_self_evaluation',
                         'clinical_classification',
                         'diagnostic_algorithm',
                         'differential_diagnosis',
                         'prognosis_cure',
                         'prognosis_survival',
                         'prognosis_recurrence',
                         'prognosis_remission',
                         'prognosis_treatment_outcome',
                         
                # Treatment fields
                'treatment_goals', 
                'treatment_strategies',
                'drug_pharma_therapy_administration_and_dosage',
                'drug_pharma_therapy_adverse_effects',
                'drug_pharma_therapy_contraindications',
                'drug_pharma_therapy_drug_interactions',
                'nursing',
                'prevention_and_control',
                'radiotherapy',
                'rehabilitation',
                'surgery',
                'dietary_supplements',
                'lifestyle_changes_smoking',
                'lifestyle_changes_alcohol',
                'lifestyle_changes_weight',
                'lifestyle_changes_diet',
                'lifestyle_changes_physical_exercise',
                'lifestyle_changes_stress',
                'lifestyle_changes_sleep',
                'treatment_algorithm',
                
                # Patient follow-up fields
                'patient_followup',
                )

alsoProvides(ISymptomsAndTreatment, form.IFormFieldProvider)

#################################  Edit Views  #################################################################
        
# Custom edit form for SymptomsAndTreament fields.
class SymptomsAndTreamentEditView(dexterity.EditForm):
    grok.context(IGuideline)
    
    grok.name('edit_symptoms_treatment')
    
    schema = ISymptomsAndTreatment
    
    additionalSchemata = []

        
# Custom edit form for RiskAssessmentAndScreening fields.
class RiskAssessmentAndScreeningEditView(dexterity.EditForm):
    grok.context(IGuideline)
    
    grok.name('edit_riskassessment_screening')
    
    schema = IRiskAssessmentAndScreening
    
    additionalSchemata = []


    
