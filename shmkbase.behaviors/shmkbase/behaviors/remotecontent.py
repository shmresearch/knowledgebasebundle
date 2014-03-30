
""" Bibliographic reference behaviour.

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


from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory

from Products.CMFCore.utils import getToolByName

from zExceptions import BadRequest
import urllib2

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab


## TODO : Conditional zcml for Products.remotefolder.


# RSS Feeds
# Using grid fields

class IRSSFeed(form.Schema):
    # Interface that defines a datagrid row.

    url = schema.URI(
        title=_(u'Feed URL'), required=True)
    name = schema.TextLine(
        title=_(u'Name'), required=True)
    #description = schema.TextLine(
    #    title=_(u'Short description'), required=False)
    

class IRemoteContentProvider(form.Schema):
    """Reused schema.
    """

    form.widget(rssfeeds=DataGridFieldFactory)
    rssfeeds = schema.List(
        title=_(u'RSS Feeds'),
        description=_(u"Add your feeds"),
        value_type=DictRow(title=_(u'RSS Feeds'), 
                           schema=IRSSFeed),
        required=False,
        default=[],
       )


# Mark these interfaces as form field providers

alsoProvides(IRemoteContentProvider, form.IFormFieldProvider)



def createRemoteFolder(container, rfolder_id, rfolder_title, rfolder_uri):
    container.invokeFactory(type_name="Remote Folder", id=rfolder_id, title=rfolder_title)
    rfolder = container[rfolder_id]
    rfolder.edit(URI = rfolder_uri)
    return rfolder


@grok.subscribe(IRemoteContentProvider, IObjectAddedEvent)
@grok.subscribe(IRemoteContentProvider, IObjectModifiedEvent)
def addRemoteFolders(obj, event):
    portal_workflow = getToolByName(obj, 'portal_workflow')

    feeds = obj.rssfeeds
    #print feeds

    for feed in feeds:
        rfolder_title = feed['name']
        rfolder_id = idnormalizer.normalize(rfolder_title.lower().replace(".", "-").replace(" ", "-"))
        if rfolder_id in obj.objectIds():  # The feed container has already been added.
            continue

        rfolder = createRemoteFolder(obj, rfolder_id, rfolder_title, feed['url'])
        portal_workflow.doActionFor(rfolder, "publish", comment="Remote folder automatically published")
        #rfolder.reindexObject()

