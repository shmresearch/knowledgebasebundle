from zope.i18nmessageid import MessageFactory

packageName = __name__
messageFactory = MessageFactory(packageName)

_ = messageFactory


#import pytz

from datetime import date
import time

from zope.interface import directlyProvides
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.site.hooks import getSite

from zope.i18n import translate

from Products.CMFCore.utils import getToolByName

import config






STUDY_CHARACTERISTICS = SimpleVocabulary([
    SimpleTerm(value=u'Case Reports',
               title=_(u'Case Reports')),
    SimpleTerm(value=u'Clinical Conference',
               title=_(u'Clinical Conference')),
    SimpleTerm(value=u'Clinical Trial',
               title=_(u'Clinical Trial')),
    SimpleTerm(value=u'Clinical Trial - Phase I',
               title=_(u'Clinical Trial, Phase I')),
    SimpleTerm(value=u'Clinical Trial - Phase II',
               title=_(u'Clinical Trial, Phase II')),
    SimpleTerm(value=u'Clinical Trial - Phase III',
               title=_(u'Clinical Trial, Phase III')),
    SimpleTerm(value=u'Clinical Trial - Phase IV',
               title=_(u'Clinical Trial, Phase IV')),
    SimpleTerm(value=u'Controlled Clinical Trial',
               title=_(u'Controlled Clinical Trial')),
    SimpleTerm(value=u'Clinical Trial - Multicenter Study',
               title=_(u'Clinical Trial, Multicenter Study')),
    SimpleTerm(value=u'Clinical Trial - Randomized Controlled Trial',
               title=_(u'Clinical Trial, Randomized Controlled Trial')),


    SimpleTerm(value=u'Comparative Study',
               title=_(u'Comparative Study')),
    SimpleTerm(value=u'Consensus Development Conference',
               title=_(u'Consensus Development Conference')),
    SimpleTerm(value=u'Evaluation Studies',
               title=_(u'Evaluation Studies')),
    SimpleTerm(value=u'In Vitro',
               title=_(u'In Vitro')),
    SimpleTerm(value=u'Meta-Analysis',
               title=_(u'Meta-Analysis')),
    SimpleTerm(value=u'Multicenter Study',
               title=_(u'Multicenter Study')),
    SimpleTerm(value=u'Scientific Integrity Review',
               title=_(u'Scientific Integrity Review')),
    SimpleTerm(value=u'Twin Study',
               title=_(u'Twin Study')),
    SimpleTerm(value=u'Validation Studies',
               title=_(u'Validation Studies')),
    SimpleTerm(value=u'Research Support - Non-U.S. Government',
               title=_(u'Research Support, Non-U.S. Government')),
    SimpleTerm(value=u'Research Support - U.S. Government',
               title=_(u'Research Support, U.S. Government')),
])

TOPICS = SimpleVocabulary([
    SimpleTerm(value=u'Epidemiology & Statistics',
               title=_(u'Epidemiology & Statistics')),
    SimpleTerm(value=u'Disease Mechanisms',
               title=_(u'Mechanisms of the disease')),
    SimpleTerm(value=u'Risk Assessment',
               title=_(u'Risk Assessment')),
    SimpleTerm(value=u'Screening',
               title=_(u'Screening')),
    SimpleTerm(value=u'Signs & Symptoms',
               title=_(u'Signs & Symptoms')),
               
    SimpleTerm(value=u'Diagnosis & Prognosis',
               title=_(u'Diagnosis & Prognosis')),
    SimpleTerm(value=u'Treatment',
               title=_(u'Treatment')),
    SimpleTerm(value=u'Patient Follow-up',
               title=_(u'Patient Follow-up')),

])

POPULATION_AGE_GROUPS = SimpleVocabulary([
    SimpleTerm(value=u'Infant - Premature',
               title=_(u'Infant, Premature')),
    SimpleTerm(value=u'Infant - Postmature',
               title=_(u'Infant, Postmature')),
    SimpleTerm(value=u'Infant - Newborn',
               title=_(u'Infant, Newborn (to 1 month)')),
    SimpleTerm(value=u'Infant',
               title=_(u'Infant (1 to 23 months)')),
    SimpleTerm(value=u'Child',
               title=_(u'Child (2 to 12 years)')),
    SimpleTerm(value=u'Adolescent',
               title=_(u'Adolescent (13 to 18 years)')),
    SimpleTerm(value=u'Adult',
               title=_(u'Adult (19 to 44 years)')),
    SimpleTerm(value=u'Middle Age',
               title=_(u'Middle Age (45 to 64 years)')),
    SimpleTerm(value=u'Aged',
               title=_(u'Aged (65 to 79 years)')),
    SimpleTerm(value=u'Aged - 80 and over',
               title=_(u'Aged, 80 and over')),
               
])

POPULATION_SEX_CATEGORIES = SimpleVocabulary([
    SimpleTerm(value=u'Men',
               title=_(u'Men')),
    SimpleTerm(value=u'Women',
               title=_(u'Women')),
    SimpleTerm(value=u'Pregnant Women',
               title=_(u'Pregnant Women')),

])


# Static vocabularies

SOCIAL_NETWORKS = SimpleVocabulary([
    SimpleTerm(value=u'Facebook',
               title=_(u'Facebook')),
    SimpleTerm(value=u'Twitter',
               title=_(u'Twitter')),
    SimpleTerm(value=u'GooglePlus',
               title=_(u'Google +')),
    SimpleTerm(value=u'LinkedIn',
               title=_(u'LinkedIn')),
               
    SimpleTerm(value=u'Youtube',
               title=_(u'Youtube')),
    SimpleTerm(value=u'Vimeo',
               title=_(u'Vimeo')),
    SimpleTerm(value=u'DailyMotion',
               title=_(u'Daily Motion')),
               
    ])

ORGANIZATION_ACTIVITY_TYPES = SimpleVocabulary([
    SimpleTerm(value=u'Learned Society',
               title=_(u'Learned Society')),
    SimpleTerm(value=u'Government Health Agency',
               title=_(u'Government Health Agency')),
    SimpleTerm(value=u'Non-Governmental Health Organization',
               title=_(u'Non-Governmental Health Organization')),
    SimpleTerm(value=u'United Nations Health Agency',
               title=_(u'United Nations Health Agency')),
               
    SimpleTerm(value=u'University Research Center',
               title=_(u'University Research Center')),
    SimpleTerm(value=u'Patient Association',
               title=_(u'Patients Association')),
               
    #SimpleTerm(value=u'',
    #           title=_(u'')),

    ])

PRESSE_ACTIVITY_TYPES = SimpleVocabulary([
    SimpleTerm(value=u'General Press',
               title=_(u'General Press')),
    SimpleTerm(value=u'Professional Press',
               title=_(u'Professional Press')),
    ])
    
COMPETITOR_TYPES = SimpleVocabulary([
    SimpleTerm(value=u'Health Management',
               title=_(u'Health Management')),
    SimpleTerm(value=u'Health Communication',
               title=_(u'Health Communication')),
    SimpleTerm(value=u'Health IT',
               title=_(u'Health IT')),
    ])

RATING_LEVELS = SimpleVocabulary([
    SimpleTerm(value=u'Very Good',
               title=_(u'Very Good')),
    SimpleTerm(value=u'Good',
               title=_(u'Good')),
    SimpleTerm(value=u'Normal',
               title=_(u'Normal')),
    SimpleTerm(value=u'Bad',
               title=_(u'Bad')),
    SimpleTerm(value=u'Very Bad',
               title=_(u'Very Bad')),
    ])
    
REVUE_PUBLISHING_FREQUENCY_TYPES = SimpleVocabulary([
    SimpleTerm(value=u'Daily',
               title=_(u'Daily (Quotidien)')),
               
    SimpleTerm(value=u'Twice Weekly',
               title=_(u'Twice Weekly (Bihebdomadaire)')),
    SimpleTerm(value=u'Weekly',
               title=_(u'Weekly (Hebdomadaire)')),
    SimpleTerm(value=u'Biweekly',
               title=_(u'Biweekly (Bimensuel)')),
               
    SimpleTerm(value=u'Monthly',
               title=_(u'Monthly (Mensuel)')),
    SimpleTerm(value=u'Bimonthly',
               title=_(u'Bimonthly (Bimestriel)')),

    SimpleTerm(value=u'Quarterly',
               title=_(u'Quarterly (Trimestriel)')),
               
    SimpleTerm(value=u'Semi-annual',
               title=_(u'Semi-annual (Semestriel)')),
    SimpleTerm(value=u'Annual',
               title=_(u'Annual (Annuel)')),
    SimpleTerm(value=u'Biannual',
               title=_(u'Biannual (Biennal)')),  

    ])


REVUE_LIBRARIES = SimpleVocabulary([
    SimpleTerm(value=u'''UniversityLibrary-Pharmacy-Besancon''',
               title=_(u'University Library - Pharmacy - Besancon')),
    SimpleTerm(value=u'''UniversityLibrary-Medicine-Geneva''',
               title=_(u'University Library - Medicine - Geneva')),
    SimpleTerm(value=u'''Library-WHO-Geneva''',
               title=_(u'Library of WHO - Geneva')),
    SimpleTerm(value=u'Other',
               title=_(u'Other library')),
    ])

REVUE_TYPES_OF_ACCESS = SimpleVocabulary([
    SimpleTerm(value=u'Electronic-RemoteAccess',
               title=_(u'Electronic Journal - Remote access')),
    SimpleTerm(value=u'Electronic-Available-Onsite',
               title=_(u'Electronic Journal - Available at the library')),
    SimpleTerm(value=u'Electronic-FullTextFree',
               title=_(u'Electronic Journal - Full Text Free')),
    SimpleTerm(value=u'Electronic-FullTextFreeAfter1Year',
               title=_(u'Electronic Journal - Full Text Free after 1 year')),
    SimpleTerm(value=u'Print-Available-Onsite',
               title=_(u'Print Journal - Available at the library')),

    ])

    
# CUTOFF_TYPES =  SimpleVocabulary([
#     SimpleTerm(value=u'Recommendation',
#                title=_(u'Recommendation')),
#     SimpleTerm(value=u'Recommendation-CutPoint',
#                title=_(u'Recommendation - Cut Point')),
#     ])


# CUTOFF_CATEGORIES =  SimpleVocabulary([
#     SimpleTerm(value=u'Health Risk Assessment',
#                title=_(u'Health Risk Assessment')),
#     SimpleTerm(value=u'Diagnostic',
#                title=_(u'Diagnostic')),
#     SimpleTerm(value=u'Prognostic',
#                title=_(u'Prognostic')),
#     SimpleTerm(value=u'Recommandations',
#                title=_(u'Recommandations (alcohol, physical activity...)')),
#     SimpleTerm(value=u'Therapeutic Goal',
#                title=_(u'Therapeutic Goal')),
#                
#     ])
    
    
# GUIDELINE_CATEGORIES =  SimpleVocabulary([
#     SimpleTerm(value=u'XX',
#                title=_(u'XX')),
#     SimpleTerm(value=u'YY',
#                title=_(u'YY')),
#     SimpleTerm(value=u'ZZ',
#                title=_(u'ZZ')),
#     SimpleTerm(value=u'XYZ',
#                title=_(u'XYZ')),
#                
#     ])


DISEASE_ATTRIBUTES = SimpleVocabulary([
    SimpleTerm(value=u'Acute Disease',
               title=_(u'Acute Disease')),
    SimpleTerm(value=u'Asymptomatic Diseases',
               title=_(u'Asymptomatic Diseases')),
    SimpleTerm(value=u'Asymptomatic Infections',
               title=_(u'Asymptomatic Infections')),
    SimpleTerm(value=u'Catastrophic Illness',
               title=_(u'Catastrophic Illness')),
    SimpleTerm(value=u'Chronic Disease',
               title=_(u'Chronic Disease')),
    SimpleTerm(value=u'Convalescence',
               title=_(u'Convalescence')),
    SimpleTerm(value=u'Critical Illness',
               title=_(u'Critical Illness')),
    SimpleTerm(value=u'Genetic Predisposition to Disease',
               title=_(u'Genetic Predisposition to Disease')),
    SimpleTerm(value=u'Emergencies',
               title=_(u'Emergencies')),
    SimpleTerm(value=u'Latrogenic Disease',
               title=_(u'Latrogenic Disease')),
    SimpleTerm(value=u'Rare Diseases',
               title=_(u'Rare Diseases')),
    SimpleTerm(value=u'Recurrence',
               title=_(u'Recurrence')),
               
    ])

    
# def CompetitorTypes(context):
#     """ Vocabulary for Competitor Types.
#     """
# 
#     return COMPETITOR_TYPES


PUBLICATION_TYPES = SimpleVocabulary([
    SimpleTerm(value=u'Abstracts',
               title=_(u'Abstracts')),
    SimpleTerm(value=u'Meeting Abstracts',
               title=_(u'Meeting Abstracts')),
    SimpleTerm(value=u'Journal Article',
               title=_(u'Journal Article')),
    SimpleTerm(value=u'Newspaper Article',
               title=_(u'Newspaper Article')),
    SimpleTerm(value=u'Article Corrected and Republished',
               title=_(u'Article Corrected and Republished')),        
    SimpleTerm(value=u'Congress',
               title=_(u'Congress')),
    SimpleTerm(value=u'Annual Report',
               title=_(u'Annual Report')),
    SimpleTerm(value=u'Comment',
               title=_(u'Comment')),      
    SimpleTerm(value=u'Editorial',
               title=_(u'Editorial')),
    SimpleTerm(value=u'Government Publication',
               title=_(u'Government Publication')),
    SimpleTerm(value=u'Guidebook',
               title=_(u'Guidebook')),
    SimpleTerm(value=u'Handbook',
               title=_(u'Handbook')),
    SimpleTerm(value=u'Guideline',
               title=_(u'Guideline')),
    SimpleTerm(value=u'Legislation',
               title=_(u'Legislation')),
    SimpleTerm(value=u'Letter',
               title=_(u'Letter')),
    SimpleTerm(value=u'Monograph',
               title=_(u'Monograph')),
    SimpleTerm(value=u'News',
               title=_(u'News')),
    SimpleTerm(value=u'Patent',
               title=_(u'Patent')),
    SimpleTerm(value=u'Pharmacopoeias',
               title=_(u'Pharmacopoeias')),
    SimpleTerm(value=u'Published Erratum',
               title=_(u'Published Erratum')),
    SimpleTerm(value=u'Review',
               title=_(u'Review')),
    SimpleTerm(value=u'Statistics',
               title=_(u'Statistics')),
    SimpleTerm(value=u'Unpublished Work',
               title=_(u'Unpublished Work')),
    SimpleTerm(value=u'Video',
               title=_(u'Video')),
    SimpleTerm(value=u'Webcast',
               title=_(u'Webcast')),
    SimpleTerm(value=u'Website',
               title=_(u'Website')),

    ])
    



def GuidelineCategories(context):
    """ Vocabulary for GuidelineCategories.
    """
 
    terms = [SimpleTerm(value=item,
                        title=translate(item, domain='shmresearch', default=item)) for item in config.GUIDELINE_CATEGORY_ITEMS]
    return SimpleVocabulary(terms)
    
    
def Specialities(context):
    """ Vocabulary for Specialities.
    """
 
    terms = [SimpleTerm(value=item,
                        title=translate(item, domain='shmresearch', default=item)) for item in config.SPECIALITY_ITEMS]
    return SimpleVocabulary(terms)
     

# Dynamic vocabularies

def Countries(context):
    """ Vocabulary for Countries.
    """

    #translate = getSite().translate

    countryutils = getToolByName(context, 'portal_countryutils')

    items = []
    if countryutils is not None:
        for country in countryutils.getCountryIsoList():
            #countryname = countryutils.getCountryByIsoCode(country)
            #print type(countryname)
            #print country[0], country[1]
            items.append((translate(country[1], domain='plonelocales', default=country[1]), country[0]))

    items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
    return SimpleVocabulary(items)


def Years(context):
    """ Vocabulary for Years.
    """
    current_time = date.fromtimestamp(time.time())
    #print dir(current_time)
    current_year = current_time.year
    #print current_year
    start_year = 1960
    year_range = range(start_year, current_year + 1)
    
    items = [SimpleTerm(str(x), str(x), str(x)) for x in year_range]
    return SimpleVocabulary(items)
        
    
def LatestYears(context):
    """ Vocabulary for Latest Years, starting in 2010.
    """
    current_time = date.fromtimestamp(time.time())
    #print dir(current_time)
    current_year = current_time.year
    #print current_year
    start_year = 2008
    year_range = range(start_year, current_year + 1)

    items = [SimpleTerm(str(x), str(x), str(x)) for x in year_range]
    return SimpleVocabulary(items)


directlyProvides(Specialities, IVocabularyFactory)

directlyProvides(Countries, IVocabularyFactory)
directlyProvides(Years, IVocabularyFactory)
directlyProvides(LatestYears, IVocabularyFactory)

# directlyProvides(CompetitorTypes, IVocabularyFactory)
