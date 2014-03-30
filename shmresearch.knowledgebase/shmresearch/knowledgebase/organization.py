
""" Organization content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobFile

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab




## Organizations Container

class IOrganizationContainer(form.Schema):

    """ An Organization container.
    """
    
    

# Organization

class IOrganization(form.Schema):

    """ A Health Organization.
    """
    
    type = schema.Choice(
            title = _(u"Organization Type"),
            vocabulary = vocab.ORGANIZATION_ACTIVITY_TYPES,
            required = True,
        )


    
# grok.templatedir("content_templates")
# 
# class View(dexterity.DisplayForm):
#     grok.context(IOrganization)
#     grok.require('zope2.View')
#     grok.template('container')

    