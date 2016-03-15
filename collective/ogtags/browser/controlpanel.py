from collective.ogtags import MessageFactory as _
from plone.app.registry.browser import controlpanel
from zope import schema
from zope.interface import Interface


class IOGTagsControlPanel(Interface):
    enabled = schema.Bool(title=_('enabled'),
            default=True)

    og_site_name = schema.TextLine(title=_('site name'),
            required=True,
            default=u'Zest')

    fb_id = schema.TextLine(title=_('facebook id'),
            required=False,
            default=u'')

    tw_id = schema.TextLine(title=_('twitter username'),
            required=False,
            default=u'')


class OGTagsCPForm(controlpanel.RegistryEditForm):
    schema = IOGTagsControlPanel
    label = _(u'OpenGraph settings')
    description = _(u'Settings for OpenGraph')


class OGTagsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = OGTagsCPForm
