
""" Contact behavior.

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




class IContactInformation(form.Schema):
    """
       Marker/Form interface for Contact Info
    """

    contactName = schema.TextLine(
        title=_(u"Contact Name"),
        description=u"",
        required=False,
    )

    contactEmail = schema.TextLine(
        title=_(u"Contact Email"),
        description=u"",
        required=False,
    )

    contactPhone = schema.TextLine(
        title=_(u"Contact Phone"),
        description=u"",
        required=False,
    )



# Mark these interfaces as form field providers

alsoProvides(IContactInformation, form.IFormFieldProvider)
