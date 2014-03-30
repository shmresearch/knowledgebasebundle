from zope.interface import Interface

from Products.CMFPlone.utils import base_hasattr
from Acquisition import aq_inner

from plone import tiles
from zope.schema import Text
from plone.app.textfield import RichText
from plone.app.textfield.interfaces import ITransformer




# class RelatedItemsTile(tiles.Tile):
# 
#     def __call__(self):
#         #text = "CLASSIFICATION TILE"
#         #return '<html><body>%s</body></html>' % text
# 
#         #self.update()
#         return self.index()

class WebUrlsTile(tiles.Tile):
    """A Web Urls tile
    """

    def weburl_items(self):
        context = aq_inner(self.context)
        items = ()

        if base_hasattr(context, 'weburls'):
            items = context.weburls

        #print items
        return items