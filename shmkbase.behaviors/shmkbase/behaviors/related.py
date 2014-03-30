
""" Related content behavior.

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

from shmkbase.behaviors import messageFactory as _

#import shmkbase.vocabularies as vocab


# Related Publications stored in the site, for Cutoffs and others
# Using grid fields

class IRelatedPublication(form.Schema):
    # Interface that defines a datagrid row.

    form.widget(related_article = 'plone.formwidget.contenttree.widget.ContentTreeWidget')
    related_article = RelationChoice(
            title = u"Related publication article",
            source = ObjPathSourceBinder(portal_type = 'shmresearch.article'),)
    pages = schema.TextLine(
                title=_(u'Pages'))
    
class IRelatedPublications(form.Schema):
    """Reused schema.
    """

    form.fieldset(
        'related',
        label=_(u'Related'),
        fields=['related_publications',],
        )
        
    form.widget(related_publications = DataGridFieldFactory)
    related_publications = schema.List(
        title=_(u'Related publications'),
        description=_(u"Add your related publications"),
        value_type=DictRow(title=_(u'Related publications'), 
                           schema=IRelatedPublication),
        required=False,
        default=[],
       )



class IRelatedItems(form.Schema):
    """Reused schema.
    """
    
    #fieldset = Fieldset('default', fields=['relatedItems'])
    form.fieldset(
        'related',
        label=_(u'Related'),
        fields=['relatedItems',],
        )
        
    #form.widget(relatedItems = DataGridFieldFactory)
    relatedItems = RelationList(
        title=_(u'label_related_items', default=u'Related Items'),
        default=[],
        value_type=RelationChoice(title=u"Related",
                      source=ObjPathSourceBinder()),
        required=False,
        )



class IRelatedHealthOrganization(form.Schema):
    """ Related Health Organization.
    """
    
    form.fieldset(
        'related',
        label=_(u'Related'),
        fields=['health_organization',],
        )
        
    # Note that this one is also used for the Cutoff and Revue...
    # Note : Later use a select field w/ autocompletewidget... !!!
    health_organization = schema.TextLine(
            title = _(u'Related Health Organization'), 
            description=u"Health Organization that has created, provided or backed this.",
            required = False,
        )


# Mark these interfaces as form field providers

alsoProvides(IRelatedPublications, form.IFormFieldProvider)
alsoProvides(IRelatedItems, form.IFormFieldProvider)
alsoProvides(IRelatedHealthOrganization, form.IFormFieldProvider)
