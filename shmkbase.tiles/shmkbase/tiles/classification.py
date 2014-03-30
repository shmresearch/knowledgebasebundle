from zope.interface import Interface

from plone import tiles
from zope.schema import Text
from plone.app.textfield import RichText
from plone.app.textfield.interfaces import ITransformer




class ContentClassificationTile(tiles.Tile):

    def __call__(self):
        #text = "CLASSIFICATION TILE"
        #return '<html><body>%s</body></html>' % text

        #self.update()
        return self.index()

#     def update(self):
#         self.portal_state = getMultiAdapter((self.context, self.request),
#                                             name=u'plone_portal_state')
#         self.context_state = getMultiAdapter((self.context, self.request),
#                                              name=u'plone_context_state')
#         self.anonymous = self.portal_state.anonymous()

#     def creator(self):
#         return self.context.Creator()
# 
#     def author(self):
#         membership = getToolByName(self.context, 'portal_membership')
#         return membership.getMemberInfo(self.creator())
# 
#     def authorname(self):
#         author = self.author()
#         return author and author['fullname'] or self.creator()




        
        
