
""" Competitor content type.

"""

from five import grok

from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form

from plone.app.textfield import RichText

from plone.namedfile.field import NamedBlobImage
from plone.namedfile.field import NamedBlobFile

from plone.app.textfield import RichText

from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory

from shmresearch.knowledgebase import messageFactory as _

import shmkbase.vocabularies as vocab



## Competitors Container

class ICompetitorContainer(form.Schema):

    """ A Competitor container.
    """



# Using grid fields

class IAnnualRevenue(form.Schema):
    # Interface that defines a datagrid row.
    
    year = schema.Choice(
            title = _(u'Year'), 
            required = False,
            vocabulary = "shmresearch.knowledgebase.LatestYears",
        )
    value = schema.TextLine(
        title=_(u'Figure / Chiffre'), required=True)
        
class IEbit(form.Schema):
    # Interface that defines a datagrid row.
    
    year = schema.Choice(
            title = _(u'Year'), 
            required = False,
            vocabulary = "shmresearch.knowledgebase.LatestYears",
        )
    value = schema.TextLine(
        title=_(u'Figure / Chiffre'), required=True)
        
class INetIncome(form.Schema):
    # Interface that defines a datagrid row.
    
    year = schema.Choice(
            title = _(u'Year'), 
            required = False,
            vocabulary = "shmresearch.knowledgebase.LatestYears",
        )
    value = schema.TextLine(
        title=_(u'Figure / Chiffre'), required=True)
        
class INumberOfEmployees(form.Schema):
    # Interface that defines a datagrid row.
    
    year = schema.Choice(
            title = _(u'Year'), 
            required = False,
            vocabulary = "shmresearch.knowledgebase.LatestYears",
        )
    value = schema.Int(
        title=_(u'Number'), required=True)
        
# Used for both the 'number_of_customers' and 'number_of_business_customers' fields
class INumberOfCustomers(form.Schema):
    # Interface that defines a datagrid row.
    
    year = schema.Choice(
            title = _(u'Year'), 
            required = False,
            vocabulary = "shmresearch.knowledgebase.LatestYears",
        )
    value = schema.Int(
        title=_(u'Number'), required=True)


# Competitor

class ICompetitor(form.Schema):

    """ A Competitor.
    """
    
    # Employees & Customers fieldset
    form.fieldset(
        'employees_and_customers',
        label=_(u'Employees & Customers'),
        fields=['number_of_employees', 'number_of_customers',
                'number_of_business_customers',],
        )

    # CompetitorInfo fieldset
    form.fieldset(
        'business_figures',
        label=_(u'Business figures'),
        fields=['annual_revenue', 'ebit','net_income',],
        )
        
    type = schema.Choice(
            title = _(u'Type of business'), 
            required = True,
            vocabulary = vocab.COMPETITOR_TYPES,
        )

    founding_year = schema.Choice(
            title = _(u'Founding year'), 
            required = False,
            vocabulary = "shmresearch.knowledgebase.Years",
        )

    publicly_traded_company = schema.Bool(
            title = _(u'Publicly traded company / Societe cotee en bourse'), 
            required = False,
        )
        
    mother_company = schema.TextLine(
            title = _(u'Subsidiary of (if applicable)'), 
            required = False,
        )

    ## Employees & Customers 

    #number_of_employees = schema.Int(
    #        title = _(u'Number of employees'), 
    #        required = False,
    #    )
    form.widget(number_of_employees=DataGridFieldFactory)
    number_of_employees = schema.List(
        title=_(u'Number of employees'),
        description=_(u"Add your Number of employees"),
        value_type=DictRow(title=_(u'Number of employees'), 
                           schema=INumberOfEmployees),
        required=False,
        default=[],
       )
       
    #number_of_customers = schema.Int(
    #        title = _(u'Number of customers'), 
    #        required = False,
    #    )
    form.widget(number_of_customers=DataGridFieldFactory)
    number_of_customers = schema.List(
        title=_(u'Number of customers'),
        description=_(u"Add your Number of customers"),
        value_type=DictRow(title=_(u'Number of customers'), 
                           schema=INumberOfCustomers),
        required=False,
        default=[],
       )

    #number_of_business_customers = schema.Int(
    #        title = _(u'Number of business customers (Corporate, Health Plan, etc)'), 
    #        required = False,
    #    )
    form.widget(number_of_business_customers=DataGridFieldFactory)
    number_of_business_customers = schema.List(
        title=_(u'Number of business customers (Corporate, Health Plan, etc)'),
        description=_(u"Add your Number of business customers"),
        value_type=DictRow(title=_(u'Number of business customers'), 
                           schema=INumberOfCustomers),
        required=False,
        default=[],
       )
       
    ## Business Figures
    
    # Data grid
    form.widget(annual_revenue=DataGridFieldFactory)
    annual_revenue = schema.List(
        title=_(u'Annual Revenue'),
        description=_(u"Add your Annual Revenue figures"),
        value_type=DictRow(title=_(u'Annual Revenue'), 
                           schema=IAnnualRevenue),
        required=False,
        default=[],
       )

    # Data grid
    form.widget(ebit=DataGridFieldFactory)
    ebit = schema.List(
        title=_(u'Earnings Before Interest And Taxes (EBIT)'),
        description=_(u"Add your EBIT figures"),
        value_type=DictRow(title=_(u'EBIT'), 
                           schema=IEbit),
        required=False,
        default=[],
       )
       
    # Data grid
    form.widget(net_income=DataGridFieldFactory)
    net_income = schema.List(
        title=_(u'Net Income'),
        description=_(u"Add your Net Income figures"),
        value_type=DictRow(title=_(u'Net Income'), 
                           schema=INetIncome),
        required=False,
        default=[],
       )


# Competitor Product

class ICompetitorProduct(form.Schema):

    """ A Competitor Product.
    """
    
