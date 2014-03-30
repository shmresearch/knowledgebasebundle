
""" Revue content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobFile

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab



# Revues Container

class IRevueContainer(form.Schema):

    """ A Revue container.
    """


# Revue

class IRevue(form.Schema):

    """ A Revue.
    """
    
    # Fieldset
    form.fieldset(
        'library',
        label=_(u'Library access'),
        fields=['library', 
                'library_other', 
                'type_of_access',
                ],
        )

    publishing_frequency = schema.Choice(
            title = _(u"Publishing Frequency"),
            vocabulary = vocab.REVUE_PUBLISHING_FREQUENCY_TYPES,
            required = False,
        )
        
    issn_electronic = schema.TextLine(
        title=_(u"ISSN - Electronic"),
        description=u"",
        required=False,
    )
    
    issn_print = schema.TextLine(
        title=_(u"ISSN - Print"),
        description=u"",
        required=False,
    )

    library = schema.Choice(
            title = _(u"Library"),
            vocabulary = vocab.REVUE_LIBRARIES,
            description=u"",
            required = False,
        )

    library_other = schema.TextLine(
        title=_(u"Name of library, if 'Other'"),
        description=u"",
        required=False,
    )

    type_of_access = schema.Choice(
            title = _(u"Type of access"),
            vocabulary = vocab.REVUE_TYPES_OF_ACCESS,
            description=u"",
            required = False,
        )


