
from types import TupleType, ListType #StringTypes, NoneType

from five import grok

from zope.interface import Interface
from zope import schema
from zope.component import adapts

#from plone.directives import dexterity, form
 
# from z3c.form.browser.textlines import TextLinesFieldWidget
# from z3c.form.browser.checkbox import CheckBoxFieldWidget
# 
# from plone.app.textfield import RichText
# 
# from plone.namedfile.field import NamedBlobFile


grok.templatedir("templates")

# class CompetitorListing(grok.View):
#     grok.context(Interface)
#     # grok.layer(INewsFlashLayer)
#     grok.require('zope2.View')


class Listing(grok.View):
    grok.context(Interface)  # or better, use the dexterity container interface ?
    grok.require('zope2.View')
    grok.template('listing')
    
    
    def getFieldData(self, item, fieldname):
        """ """
        data = getattr(item, fieldname, '')
            
        # Treat special cases
        
        if fieldname == 'publication_type' and data == 'Publication type 1':
            data = 'N/A'
            
        if fieldname in ['specialities',  
                         'disease_and_health_condition_categories',
                         'levels_of_prevention',
                         'substances',]:                    # value is of List or Tuple Type
                                                                      # but beware of Missing Values !
            if data != [] or data != ():
                try:    # to avoid the "TypeError: 'Missing.Value' object is unsubscriptable" error here.
                    #data = data[0]
                    data = ', '.join(data)
                except:
                    data = ''
            else:
                data = ''   
                
        if fieldname == 'weburls':
            if len(data):
                data = data[0]['url']
                data = '<a href="%s" target="_blank" >Website</a>' % data
            else:
                data = ''

        if fieldname in ['number_of_employees', 'number_of_customers',]:
            if not (data is None or data == []):
                print data
                try:
                    data = data[0]
                    data = '%s <em>in %s</em>' % (str(data['value']),data['year'])
                except:
                    data = ''
            else:
                data = ''
        
        return data
            
    def getFields(self):
        context = self.context
        fields = [('Title', 'Name / Title'), ]
        
        main_health_fields = [('specialities', 'Specialty'), 
                              ('disease_and_health_condition_categories', 'Disease & Health conditions'),
                              ]
                          
        article_fields = main_health_fields + [
                          ('health_organization', 'Health Organization'),
                          ('publication_type', 'Type of publication'),
                          ('journal', 'Journal'),
                          ('year', 'Year'),
                          ('rating', 'Rating'),
                         ]
                         
        cutoff_fields = main_health_fields + [
                          ('levels_of_prevention', 'Level of prevention'),
                          ('substances', 'Substance categories'),
                          ('health_organization', 'Health Organization'),
                          ('year', '(Year of the publication - TODO)'),
                          ('rating', 'Rating'),
                         ]
                         
        guideline_fields = main_health_fields + [
                          ('levels_of_prevention', 'Level of prevention'),
                          #('rating', 'rating'),
                         ]
                         
        questionnaire_fields = main_health_fields + [
                          #('publication_type', 'publication_type'),
                          #('rating', 'rating'),
                         ]
                         
        # Do not use main_health_fields
        competitor_fields = [
                          ('type', 'Type of business'),
                          ('country', 'Country'),
                          ('rating', 'Rating'),
                          ('number_of_employees', 'Number of employees'),
                          ('number_of_customers', 'Number of customers'),
                          ('weburls', ''),
                         ]
                         
        # Do not use main_health_fields
        organization_fields = [
                          ('type', 'Type of organization'),
                          ('specialities', 'Specialty'),
                          ('country', 'Country'),
                          #('xxx', 'xxx'),
                          ('weburls', ''),
                         ]

        # Do not use main_health_fields
        revue_fields = [
                          #('type', 'Type of revue'),
                          ('specialities', 'Specialty'),
                          ('health_organization', 'Health Organization'),
                          ('country', 'Country'),
                          ('weburls', ''),
                         ]
                         
        # Do not use main_health_fields
        presse_fields = [
                          ('type', 'Type of press actor'),
                          ('country', 'Country'),
                          ('weburls', ''),
                         ]
                         
        # Do not use main_health_fields
        marketingkit_fields = [
                          ('product_category', 'Product category'),
                          ('product_market_sector', 'Market sector'),
                         ]
                         
        if context.portal_type == 'shmresearch.articlecontainer':
            fields = fields + article_fields
        elif context.portal_type == 'shmresearch.competitorcontainer':
            fields = fields + competitor_fields
        elif context.portal_type in ['shmresearch.cutoffitemcontainer', 
                                     'shmresearch.definitionitemcontainer']:
            fields = fields + cutoff_fields        
        elif context.portal_type == 'shmresearch.guidelinecontainer':
            fields = fields + guideline_fields
        elif context.portal_type == 'shmresearch.questionnairecontainer':
            fields = fields + questionnaire_fields
        elif context.portal_type == 'shmresearch.organizationcontainer':
            fields = fields + organization_fields
        elif context.portal_type == 'shmresearch.revuecontainer':
            fields = fields + revue_fields
        elif context.portal_type == 'shmresearch.pressecontainer':
            fields = fields + presse_fields
        elif context.portal_type == 'shmresearch.marketingkitcontainer':
            fields = fields + marketingkit_fields
            
        return fields

