
""" Questionnaire content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobFile

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab




## Questionnaires Container

class IQuestionnaireContainer(form.Schema):

    """ A Questionnaire container.
    """
    

# Questionnaire

class IQuestionnaire(form.Schema):

    """ A Questionnaire.
    """

    text = RichText(
            title = _(u'Text'), 
            required = False,
        )


# grok.templatedir("content_templates")
# 
# class View(dexterity.DisplayForm):
#     grok.context(IQuestionnaire)
#     grok.require('zope2.View')
#     grok.template('item')
    