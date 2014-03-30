from zope.i18nmessageid import MessageFactory

packageName = __name__
messageFactory = MessageFactory(packageName)

import sys

#import patches


from plone.autoform.interfaces import WIDGETS_KEY
from plone.directives.form.schema import TEMP_KEY
from plone.app.dexterity.behaviors.metadata import ICategorization
from zope import schema as _schema

#_directives_values = ICategorization.queryTaggedValue(TEMP_KEY)
#_directives_values.setdefault(WIDGETS_KEY, {})
#widget = 'collective.z3cform.widgets.token_input_widget.TokenInputFieldWidget'
#_directives_values[WIDGETS_KEY]['subjects'] = widget
#_schema.getFields(ICategorization)['subjects'].index_name = 'Categories'
#_schema.getFields(ICategorization)['subjects'].title = u'Keywords'

#from shmkbase.guideline import content
#sys.modules['shmresearch.knowledgebase.guideline'] = content
