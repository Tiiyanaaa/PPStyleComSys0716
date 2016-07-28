from collective.grok import gs
from PPStyleComSys0716.app import MessageFactory as _

@gs.importstep(
    name=u'PPStyleComSys0716.app', 
    title=_('PPStyleComSys0716.app import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('PPStyleComSys0716.app.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
