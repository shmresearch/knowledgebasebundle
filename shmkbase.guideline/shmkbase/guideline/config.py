
## Guideline schema config


GUIDELINE_FIELD_GROUPS = [
           'grade_evidence_level',
           'diagnosis_and_prognosis',
           'symptoms',
           'patient_followup',
           'disease_mechanisms',
           'epidemio',
           'treatment',
           'screening',
           'riskassessment',
          ]



GUIDELINE_FIELDS = {
        
           'grade_evidence_level': (u'Grade / Level of Evidence',
                        ['grade_evidence_level',
                        ]),

           'diagnosis_and_prognosis': (u'Diagnosis & Prognosis',
                        ['diagnosis_physical_examination',
#                         'diagnostic_techniques_clinical_laboratory',
#                         'diagnostic_techniques_imaging',
#                         'diagnostic_techniques_cardiovascular',
#                         'diagnostic_techniques_digestive_system',
#                         'diagnostic_techniques_endocrine',
#                         'diagnostic_techniques_obstetrical_and_gynecological',
#                         'diagnostic_techniques_ophtalmological',
#                         'diagnostic_techniques_radioisotope',
#                         'diagnostic_techniques_respiratory_system',
#                         'diagnostic_techniques_surgical',
#                         'diagnostic_techniques_urological',
#                         'diagnostic_techniques_monitoring_physiologic',
#                         'diagnostic_techniques_self_evaluation',
                         
                         'clinical_classification',
                         'diagnostic_algorithm',
                         'differential_diagnosis',
                        
                         'prognosis_cure',
                         'prognosis_survival',
                         'prognosis_recurrence',
                         'prognosis_remission',
                         'prognosis_treatment_outcome',
                                              
                        ]),

           'symptoms': (u'Signs & Symptoms',
                        ['signs_and_symptoms',
                        ]),

           'patient_followup': (u'Patient follow-up',
                        ['patient_followup',
                        ]),
                        

           'disease_mechanisms': (u'Mechanisms of the disease',
                        ['disease_attributes',
                         'physiopathology_or_pathologic_processes',
                         'complications',
                        ]),

           'epidemio': (u'Epidemiology & Statistics',
                        ['disease_incidence', 
                         'disease_mortality',
                         'disease_prevalence',
                         'risk_of_being_diagnosed',
                         'risk_of_dying',
                         'lifetime_risk_of_being_diagnosed',
                         'lifetime_risk_of_dying',
                         'age_at_diagnosis',
                         'age_at_death',
                         'survival_rate',
                         'median_survival_times',
                        ]),
                       
           'treatment': (u'Treatment',
                         ['treatment_goals', 
                          'treatment_strategies',
                          
                          'drug_pharma_therapy_administration_and_dosage',
                          'drug_pharma_therapy_adverse_effects',
                          'drug_pharma_therapy_contraindications',
                          'drug_pharma_therapy_drug_interactions',
                          #'drug_pharma_therapy_',
                          #'drug_pharma_therapy_',
                          #'drug_pharma_therapy_',
                          
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
                          
                         # 'follow_up',
                        ]),

           'screening': (u'Screening',
                        ['screening_goals',
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
                        
                        
                        ]),
                        
           'riskassessment': (u'Risk Assessment',
                        ['risk_factors_age',
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
    
                        ]),
                        
                        
                        
                        
          }



## RISK ASSESSMENT

# Risk Factors - Age
# 
# Risk Factors - Family History
# 
# Risk Factors - Personal History
# 
# -        Genetic / Genomic
# 
# -        Smoking habits
# 
# -        Alcohol consumption
# 
# -        Dietary habits
# 
# -        Amount of Physical exercise
# 
# -        Obesity /Overweight
# 
# -        Sleep habits / disorders
# 
# -        Stress
# 
# -        Drug/substance intake
# 
# -        Disease
# 
# -        Infectious Agents
# 
# -        Other risk factors
# 
#  
# 
# RISK MARKERS
# 
#  
# 
# RISK STRATIFICATION (Risk Levels)

 

## TREATMWENT

# Goals of Treatment
# Treatment Strategies
# Therapy - Drug / Pharmacological Therapy
# Therapy -   Nursing
# Therapy -   Prevention & Control
# Therapy -   Radiotherapy
# Therapy -   Rehabilitation
# Therapy -   Surgery 
# Therapy -   Dietary Supplements

# Therapy -   Lifestyle Changes -  Smoking Cessation
# Therapy -   Lifestyle Changes -  Alcohol Consumption
# Therapy -   Lifestyle Changes  - Weight Management
# Therapy -   Lifestyle Changes  - Diet Changes
# 
# Therapy -   Lifestyle Changes  - Physical Exercise
# 
# Therapy -   Lifestyle Changes  - Stress
# 
# Therapy -   Lifestyle Changes -  Sleep
# 
# Follow-up
# 


