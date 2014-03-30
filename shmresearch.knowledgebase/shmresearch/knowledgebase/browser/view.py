

from five import grok

from zope.interface import Interface
from zope import schema
from zope.component import adapts

from plone.directives import dexterity, form
 
# from z3c.form.browser.textlines import TextLinesFieldWidget
# from z3c.form.browser.checkbox import CheckBoxFieldWidget
# 
# from plone.app.textfield import RichText
# 
# from plone.namedfile.field import NamedBlobFile


grok.templatedir("templates")

class Item(dexterity.DisplayForm):
    grok.context(Interface)   # or better, use the dexterity item interface ?
    grok.require('zope2.View')
    grok.template('item')

    
class Container(dexterity.DisplayForm):
    grok.context(Interface)  # or better, use the dexterity container interface ?
    grok.require('zope2.View')
    grok.template('container')
    
        

        
