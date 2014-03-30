from zope.interface import Interface

from Products.CMFPlone.utils import base_hasattr
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName

from plone import tiles
from zope.schema import Text
from plone.app.textfield import RichText
from plone.app.textfield.interfaces import ITransformer

from shmresearch.knowledgebase.competitor import ICompetitorProduct



# class RelatedItemsTile(tiles.Tile):
# 
#     def __call__(self):
#         #text = "CLASSIFICATION TILE"
#         #return '<html><body>%s</body></html>' % text
# 
#         #self.update()
#         return self.index()

class RelatedItemsTile(tiles.Tile):
    """A related items tile
    """

    def related_items(self):
        context = aq_inner(self.context)
        related = ()

        if base_hasattr(context, 'relatedItems'):
            related = context.relatedItems

        return related
        
        
class RelatedCompetitorProductsTile(tiles.Tile):
    """A Related Competitor Products tile, with the list of items based on search.
    """

    def products(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        
        product_category = ''
        if base_hasattr(context, 'product_category'):
            product_category = context.product_category

        query = dict(
            object_provides = ICompetitorProduct.__identifier__,
            SearchableText = product_category,
        )

        brains = catalog(query)
        #print brains
        return brains
        
        