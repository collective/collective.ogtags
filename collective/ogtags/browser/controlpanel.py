from collective.ogtags import MessageFactory as _
from plone.app.registry.browser import controlpanel
from zope import schema
from zope.interface import Interface


class IOGTagsControlPanel(Interface):
    enabled = schema.Bool(title=_('Enabled'),
            default=False)

    og_site_name = schema.TextLine(title=_('Site name'),
            required=False,
            default=u'')

    fb_username = schema.TextLine(title=_('Facebook username'),
            required=False,
            default=u'')

    fb_id = schema.TextLine(title=_('Facebook app id'),
            required=False,
            default=u'')

    tw_id = schema.TextLine(title=_('Twitter username'),
            description=_('example: @zestsoftware'),
            required=False,
            default=u'')


class OGTagsCPForm(controlpanel.RegistryEditForm):
    schema = IOGTagsControlPanel
    label = _(u'OpenGraph settings')
    description = _(u'Settings for OpenGraph')


class OGTagsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = OGTagsCPForm
