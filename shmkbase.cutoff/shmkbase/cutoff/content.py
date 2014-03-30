
""" Cutoff content types.

"""

from five import grok

from zope import schema
from zope.component import adapts

from zope.app.container.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from z3c.form.interfaces import IEditForm
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from plone.app.textfield import RichText

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

#from shmkbase.guideline import config as guideline_config

from shmkbase.cutoff import messageFactory as _



## Cutoffs Container

class ICutoffItemContainer(form.Schema):

    """ A cutoff item container.
    """


## Cutoff

class IBaseCutoffItem(form.Schema):

    title = schema.TextLine(
            title = _(u'Name'), 
            required = True,
        )
        
    text = RichText(
            title = _(u'Text'), 
            required = False,
        )
        

# Cutoff Item

class ICutoffItem(IBaseCutoffItem):

    """ A cutoff item.
    """


## Definitions Container

class IDefinitionItemContainer(form.Schema):

    """ A definition item container.
    """

# Definition Item

class IDefinitionItem(IBaseCutoffItem):

    """ A definition item.
    """


    
    
# grok.templatedir("content_templates")
# 
# class View(dexterity.DisplayForm):
#     grok.context(IBaseCutoffItem)
#     grok.require('zope2.View')
#     grok.template('item')


