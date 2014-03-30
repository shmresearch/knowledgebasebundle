#from zope.component import getUtility
#from zope.event import notify

#from z3c.form import form, button
#from plone.z3cform import layout

from five import grok

from plone.directives import dexterity

#from plone.dexterity.browser.base import DexterityExtensibleForm

from Products.CMFCore.utils import getToolByName

from shmkbase.behaviors.categorization import IClassification, ISHMContentClassification

from plone.dexterity.interfaces import IDexterityContent


# Custom edit form for Classification fields for Articles, Guidelines, etc...
class ClassificationEditView(dexterity.EditForm):

    grok.context(IDexterityContent)  # Trying to provide this for all contexts! WORKING!!!
    
    grok.name('edit_classifiers')
    
    @property
    def schema(self):
        #fti = getUtility(IDexterityFTI, name=self.portal_type)
        #return fti.lookupSchema()
        if self.context.portal_type in ('shmresearch.article',
                                        'shmresearch.cutoffitem',
                                        'shmresearch.definitionitem',
                                        'shmresearch.questionnaire',
                                        ):
            return IClassification
        else:
            return ISHMContentClassification
    
    additionalSchemata = []

