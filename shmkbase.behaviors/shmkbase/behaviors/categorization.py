
""" Categorization / Classification behaviours.

"""

from five import grok

from zope import schema
from zope.component import adapts

#from zope.component import adapter
#from zope.interface import implementer

from zope.interface import alsoProvides
from zope.interface import implements
from zope.interface import invariant, Invalid
from zope.interface import Interface

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

from zope.app.container.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from z3c.form.interfaces import IEditForm

from z3c.relationfield.schema import RelationChoice, RelationList

from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory

from plone.formwidget.autocomplete.widget import (
    AutocompleteMultiFieldWidget,
    )
from plone.formwidget.contenttree import (
    ContentTreeFieldWidget,
    PathSourceBinder,
    ObjPathSourceBinder,
    )

from z3c.form.browser.textlines import TextLinesFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from plone.directives import form

from plone.i18n.normalizer import idnormalizer

from plone.indexer import indexer
from plone.app.dexterity.behaviors.metadata import ICategorization
from plone.dexterity.interfaces import IDexterityContent

from plone.namedfile.field import NamedBlobImage
from plone.namedfile.field import NamedBlobFile

from plone.app.textfield import RichText

from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory

from collective.z3cform.widgets.multicontent_search_widget import MultiContentSearchFieldWidget
from collective.z3cform.widgets.enhancedtextlines import EnhancedTextLinesFieldWidget

from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from Products.CMFCore.utils import getToolByName

from zExceptions import BadRequest
import urllib2

from shmkbase.behaviors import messageFactory as _

import shmkbase.vocabularies as vocab





################################# BBB #################################
class IPublicationCategorization(form.Schema):

    """ Categorization schema class, kept for BBB.

    """

#####################################################################



# 1/ Study Characteristics Categorization / Qualification

# Using grid fields
class INumberOfPeopleByGroup(form.Schema):
    # Interface that defines a datagrid row.

    group = schema.TextLine(
        title=_(u'Group'), 
        required=False,
        )
        
    number = schema.TextLine(
        title=_(u'Number of people'), 
        required=False,
        )
        
class IStudyCharacteristicsCategorization(form.Schema):

    """ Study Characteristics / Qualification schema.

    """

    # study_characteristics fieldset
    form.fieldset(
        'study_qualification',
        label=_(u'Study Qualification'),
        fields=['publication_type',
                'study_characteristics',
                'total_number_of_people',
                'number_of_people_in_the_different_groups',
                'level_of_evidence',
                'class_of_recommendations',
                ],
        )

    # See later how to have this one only for only Articles and Guidelines !!!
    form.omitted('publication_type')
    publication_type = schema.Choice(
            title = _(u"Publication Type"),
            vocabulary = vocab.PUBLICATION_TYPES,
            required = False,
        )    

    form.omitted('study_characteristics')
    form.widget(study_characteristics = CheckBoxFieldWidget)
    study_characteristics = schema.List(
        title = _(u"Study characteristics"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary = vocab.STUDY_CHARACTERISTICS), # 
        required = False, #True,
        )

    form.omitted('total_number_of_people')
    total_number_of_people = schema.TextLine(
            title = _(u'Total number of people'), 
            required = False,
        )
        
    form.omitted('number_of_people_in_the_different_groups')
    form.widget(number_of_people_in_the_different_groups=DataGridFieldFactory)
    number_of_people_in_the_different_groups = schema.List(
        title=_(u' Number of people in the different group'),
        description=_(u"Add the number of people in the different group"),
        value_type=DictRow(title=_(u' Number of people in the different group'), 
                           schema=INumberOfPeopleByGroup),
        required=False,
        default=[],
       ) 
       
    form.omitted('level_of_evidence')
    level_of_evidence  = schema.Choice(
            title = _(u"Level of evidence"),
            vocabulary = SimpleVocabulary([SimpleTerm(value=u'High',
                                                      title=_(u'High')),
                                           SimpleTerm(value=u'Moderate',
                                                      title=_(u'Moderate')),
                                           SimpleTerm(value=u'Low',
                                                      title=_(u'Low')),
                                           ]),
            required = False,
        )  
       
    form.omitted('class_of_recommendations')
    class_of_recommendations  = schema.Choice(
            title = _(u"Class of recommendations"),
            vocabulary = SimpleVocabulary([SimpleTerm(value=u'recommanded',
                                                      title=_(u'Is recommanded')),
                                           SimpleTerm(value=u'should_be_considered',
                                                      title=_(u'Should be considered')),
                                           SimpleTerm(value=u'may_be_considered',
                                                      title=_(u'May be considered')),
                                           SimpleTerm(value=u'not_recommanded',
                                                      title=_(u'Is not recommanded')),
                                           SimpleTerm(value=u'should_be_avoided',
                                                      title=_(u'Should be avoided')),
                                           SimpleTerm(value=u'must_be_avoided',
                                                      title=_(u'Must be avoided')),
                                           ]),
            required = False,
        ) 
        
    
# 2/ General Categorization / Specialties

class IGeneralCategorization(form.Schema):

    """ General categorization schema, including Specialties.

    """

    form.fieldset(
        'specialties',
        label=_(u'Specialties'),
        fields=['specialities',],
        )
        
    form.omitted('specialities')
    form.widget(specialities=CheckBoxFieldWidget)   # beware the spelling here: 'specialities'
    specialities = schema.List(
        title = _(u"Specialties"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary = "shmresearch.knowledgebase.Specialities"),
        missing_value=[],
        required = False, #True,
        )


# 3/ Disease and Health Condition
                
class IDiseaseAndHealthConditionCategorization(form.Schema):

    """ DiseaseAndHealthCondition Categorization schema.
    """

    form.fieldset(
        'disease_and_health_condition',
        label=_(u'Disease and Health Condition'),
        fields=[
                'disease_and_health_condition_categories', 
                'levels_of_prevention',
                'subject', #'mesh_keywords',
                'substances',
                'topics',
                ],
        )
        
    form.omitted('disease_and_health_condition_categories')
    form.widget(disease_and_health_condition_categories = EnhancedTextLinesFieldWidget)
    disease_and_health_condition_categories = schema.Tuple(
            title=_(u"Disease and health condition categories (Mesh)"),
            value_type=schema.TextLine(),
            missing_value=(),
            required = False,
            )

    form.omitted('levels_of_prevention')
    form.widget(levels_of_prevention=CheckBoxFieldWidget) 
    levels_of_prevention = schema.List(
        title = _(u"levels_of_prevention"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary =  SimpleVocabulary([SimpleTerm(value=u'Primary',
                                                      title=_(u'Primary prevention')),
                                           SimpleTerm(value=u'Secondary',
                                                      title=_(u'Secondary prevention')),
                                           SimpleTerm(value=u'Tertiary',
                                                      title=_(u'Tertiary prevention')),
                                           ]),
            ),
        missing_value=[],
        required = False, #True,
        )
        
    # Replacement for Plone's subject/keywords field.
    form.omitted('subject')
    form.widget(subject = EnhancedTextLinesFieldWidget)
    subject = schema.Tuple(
            title=_(u"Keywords (MeSH)"),
            value_type=schema.TextLine(),
            missing_value=(),
            required = False,
            )

    form.omitted('substances')
    form.widget(substances = EnhancedTextLinesFieldWidget)
    substances = schema.Tuple(
            title=_(u"Substances - Chemicals and Drugs Categories (MeSH)"),
            value_type=schema.TextLine(),
            missing_value=(),
            required = False,
            )

    form.omitted('topics')
    form.widget(topics = CheckBoxFieldWidget)
    topics = schema.List(
        title = _(u"Topics"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary = vocab.TOPICS), # 
        required = False, #True,
        )



# 4/ Target Population
                
class ITargetPopulation(form.Schema):
    """ """

    form.fieldset(
        'target_population',
        label=_(u'Target Population'),
        fields=[
                'target_population_age_groups',
                'target_population_sex_categories',
                ],
        )
        
    form.omitted('target_population_age_groups')
    form.widget(target_population_age_groups = CheckBoxFieldWidget)
    target_population_age_groups = schema.List(
        title = _(u"Target population - Age groups"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary = vocab.POPULATION_AGE_GROUPS), # 
        required = False, #True,
        )

    form.omitted('target_population_sex_categories')
    form.widget(target_population_sex_categories = CheckBoxFieldWidget)
    target_population_sex_categories = schema.List(
        title = _(u"Target population - Sex categories"),
        value_type = schema.Choice(
         #  title = _(u"Selection"),
            vocabulary = vocab.POPULATION_SEX_CATEGORIES), # 
        required = False, #True,
        )



alsoProvides(IGeneralCategorization, form.IFormFieldProvider)
alsoProvides(IStudyCharacteristicsCategorization, form.IFormFieldProvider)
alsoProvides(IDiseaseAndHealthConditionCategorization, form.IFormFieldProvider)
alsoProvides(ITargetPopulation, form.IFormFieldProvider)

#################################

## Behavior just needed to build a specific ClassificationEditView!!!
# (But not to be set explicitely on an FTI/object. So we don't register it in the configure.zcml!)
# Grouping the previous ones...


class ISHMContentClassification(ITargetPopulation,
                      IDiseaseAndHealthConditionCategorization, 
                      IGeneralCategorization,
                      ):
    """ Grouped behaviour for SHM authord content.
        Does not contain IStudyCharacteristicsCategorization.
    """

    form.no_omit(IEditForm, 
#                 'publication_type',
#                 'study_characteristics',
#                 'total_number_of_people',
#                 'number_of_people_in_the_different_groups',
#                 'level_of_evidence',
#                 'class_of_recommendations',
                
                'specialities',
                
                'disease_and_health_condition_categories',
                'levels_of_prevention',
                'subject', #'mesh_keywords',
                'substances',
                'topics',
                
                'target_population_age_groups',
                'target_population_sex_categories',
                )

alsoProvides(ISHMContentClassification, form.IFormFieldProvider)


class IClassification(ISHMContentClassification,
                      IStudyCharacteristicsCategorization):
    """ Grouped behaviour for non-SHM content.
        Contains IStudyCharacteristicsCategorization too.
    """
    form.no_omit(IEditForm, 
                'publication_type',
                'study_characteristics',
                'total_number_of_people',
                'number_of_people_in_the_different_groups',
                'level_of_evidence',
                'class_of_recommendations',
                
#                 'specialities',
#                 
#                 'disease_and_health_condition_categories',
#                 'levels_of_prevention',
#                 'mesh_keywords',
#                 'topics',
#                 
#                 'target_population_age_groups',
#                 'target_population_sex_categories',
                )

alsoProvides(IClassification, form.IFormFieldProvider)