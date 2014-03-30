
""" Social networks behaviors.

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

from z3c.relationfield.schema import RelationChoice, RelationList

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

from Products.CMFCore.utils import getToolByName

from zExceptions import BadRequest
import urllib2

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab



# Using grid fields

class ISocialNetwork(form.Schema):
    # Interface that defines a datagrid row.

    type = schema.Choice(
            title = _(u"Social Network"),
            vocabulary = vocab.SOCIAL_NETWORKS,
        ) 
    account = schema.TextLine(
        title=_(u'Account ID'), required=True)
    #name = schema.TextLine(
    #    title=_(u'Name'), required=True)
    description = schema.TextLine(
        title=_(u'Short description'), required=False)


class ISocialMedia(form.Schema):
    """ Social Media schema.

    """
        
    # Data grids

    form.widget(socialnetworks=DataGridFieldFactory)
    socialnetworks = schema.List(
        title=_(u'Social Network Accounts'),
        description=_(u"Add your Social Networks"),
        value_type=DictRow(title=_(u'Social Networks'), 
                           schema=ISocialNetwork),
        required=False,
        default=[],
       )    


# Mark these interfaces as form field providers

alsoProvides(ISocialMedia, form.IFormFieldProvider)
