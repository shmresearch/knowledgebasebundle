
from Products.remotefolder.content.remotefolder import RemoteFolder
from Products.remotefolder.content.remotefolder import ContentParser


def addPloneObjects(self, feed):
    """From a feed object, create plone content in the remote folder"""
    container = self
    result = ""
    feedItem = None
    id = ""
    type = self._detectType(feed)
    
    #to print feed properties
    #for obj in dir(feed):
        #printer = obj + " --- " + self._detectType(feed) 
        #print(printer)
        
    if feed.needs_update:
        feed.update()
    #else:
    #    """If there is no update, do nothing"""
    #    #return result
    
    for item in feed.items:
        feedItem = ContentParser(item, type)
        result += "<h1>" + feedItem.title  + "</h1>" + "<BR />" + feedItem.description + "<BR />"
        #ADD PLONE CONTENT HERE
        title = feedItem.title
        id = idnormalizer.normalize(title + "%s"%(feedItem.updated, ))
        
        if hasattr(container, id):
            #If the item exists we continue to the next one
            continue
    
        #And now we create our content
        if type is "Other":
            createRSSDocument(container, feedItem, id)
        elif type is "Flickr":
            self._createImage(container, feedItem, id)
    
    return result

    
def createRSSDocument(container, feedItem, id):
    container.invokeFactory(type_name="shmresearch.rssdocument", 
                            id=id, 
                            title=feedItem.title)
    obj = container[id]
    #obj.setText(feedItem.description)
    obj.url = feedItem.url
    obj.portal_workflow.doActionFor(obj, "publish", comment="Remote content automatically published")

 
 ## Disabled this for now. Requires more testing... 
#RemoteFolder.addPloneObjects = addPloneObjects
