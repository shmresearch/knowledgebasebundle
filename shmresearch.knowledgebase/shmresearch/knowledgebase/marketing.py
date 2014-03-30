
""" ProductMarketingSheet content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobFile

from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from shmresearch.knowledgebase import messageFactory as _

from collective.z3cform.addablechoice.widget import AddableChoiceFieldWidget

import shmkbase.vocabularies as vocab



# MARKET_SECTORS = SimpleVocabulary([
#     SimpleTerm(value=u'Employers',
#                title=_(u'Employers')),
#     SimpleTerm(value=u'Professional Organizations',
#                title=_(u'Professional Organizations')),
#     SimpleTerm(value=u'Insurrance Companies',
#                title=_(u'Insurrance Companies')),
#     SimpleTerm(value=u'Brokers',
#                title=_(u'Brokers')),
#     SimpleTerm(value=u'Consultants',
#                title=_(u'Consultants')),
#     SimpleTerm(value=u'Healthcare Providers',
#                title=_(u'Healthcare Providers')),
#     SimpleTerm(value=u'Pharmaceutical Companies',
#                title=_(u'Pharmaceutical Companies')),
#     SimpleTerm(value=u'Public Sector & Government',
#                title=_(u'Public Sector & Government')),
# 
#     ])



## MarketingKit Container

class IMarketingKitContainer(form.Schema):

    """ A MarketingKit container.
    """
    

# MarketingKit

class IMarketingKit(form.Schema):

    """ A Marketing Kit.
    """

    form.fieldset(
        'print',
        label=_(u'Print-specific'),
        fields=['test_print',],
        )
        
    form.fieldset(
        'video',
        label=_(u'Video-specific'),
        fields=['test_video',],
        )
        
#     form.fieldset(
#         'categorization',
#         label=_(u'Categorization'),
#         fields=['product_category',],
#         )
        
    form.widget(product_category = AddableChoiceFieldWidget)        
    product_category = schema.TextLine(
            title = _(u"Product category - For checking competing products"),
            #description=u"Keyword allowing you to get the list of similar competitors products.",
            required = False,
            default = u'',
        )

    form.widget(product_market_sector = AddableChoiceFieldWidget)        
    product_market_sector = schema.TextLine(
            title = _(u"What market is the product for ?"),
            required = False,
            default = u'',
        )

    product_solving_issue = RichText(     # better name ???
            title = _(u'What problem is the product solving ?'), 
            required = False,
        )

    product_description = RichText(
            title = _(u'Product Description'), 
            required = False,
        )

    product_goals = RichText(
            title = _(u'Product Goals'), 
            required = False,
        )

    product_results = RichText(
            title = _(u'Product Results'), 
            required = False,
        )

    product_differentiators = RichText(
            title = _(u'Our Difference'), 
            required = False,
        )
        
    product_faq = RichText(
            title = _(u'FAQs'), 
            required = False,
        )

    product_slogans = schema.Text(
        title=_(u"Slogan(s)"),
        description=u"",
        required=False,
    )

    ## Tests...
    test_print = RichText(
            title = _(u'Test for Print'), 
            required = False,
        )
        
    test_video = RichText(
            title = _(u'Test for Video'), 
            required = False,
        )
        
    