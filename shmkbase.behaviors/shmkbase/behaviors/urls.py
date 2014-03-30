
""" Web URLs behaviour.

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



class IWebURL(form.Schema):
    # Interface that defines a datagrid row.
    
    url = schema.URI(
        title=_(u'URL'), required=True)
    name = schema.TextLine(
        title=_(u'Name'), required=True)
    description = schema.TextLine(
        title=_(u'Short description'), required=False)


class IWebURLs(form.Schema):
    """ Web Resource URLs schema.

    """
        
    # Data grids

    form.widget(weburls=DataGridFieldFactory)
    weburls = schema.List(
        title=_(u'Web URLs'),
        description=_(u"Add your web URLs"),
        value_type=DictRow(title=_(u'Web URLs'), 
                           schema=IWebURL),
        required=False,
        default=[],
       )
    


# Mark these interfaces as form field providers

alsoProvides(IWebURLs, form.IFormFieldProvider)
