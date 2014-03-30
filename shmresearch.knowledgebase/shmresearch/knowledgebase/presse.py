
""" Presse content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobFile

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab


# Presse actors Container

class IPresseContainer(form.Schema):

    """ A Presse actor container.
    """
    
    
# Presse

class IPresse(form.Schema):

    """ A Presse actor.
    """
    
    type = schema.Choice(
            title = _(u"Presse Type"),
            vocabulary = vocab.PRESSE_ACTIVITY_TYPES,
            required = True,
        )

# grok.templatedir("content_templates")
# 
# class View(dexterity.DisplayForm):
#     grok.context(IPresse)
#     grok.require('zope2.View')
#     grok.template('container')
   