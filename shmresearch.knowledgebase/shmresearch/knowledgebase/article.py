
""" Article content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

#from plone.directives import dexterity, form
from plone.supermodel import model

from z3c.form.browser.textlines import TextLinesFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobFile

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab


## Articles Container

class IArticleContainer(model.Schema):

    """ An Article container.
    """
    
    

# Article

class IArticle(model.Schema):

    """ A Publication Article.
    """
    

# 
# grok.templatedir("content_templates")
# 
# class View(dexterity.DisplayForm):
#     grok.context(IArticle)
#     grok.require('zope2.View')
#     grok.template('item')

    
    
        
        
        
