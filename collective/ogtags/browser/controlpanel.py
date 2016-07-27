from collective.ogtags import MessageFactory as _
from plone.app.registry.browser import controlpanel
from zope import schema
from zope.interface import Interface


class IOGTagsControlPanel(Interface):
    enabled = schema.Bool(
        title=_(u'Enabled'),
        default=True)

    og_site_name = schema.TextLine(
        title=_(u'Site name'),
        required=False,
        default=u'')

    fb_username = schema.TextLine(
        title=_(u'Facebook username'),
        required=False,
        default=u'')

    fb_id = schema.TextLine(
        title=_(u'Facebook app id'),
        required=False,
        default=u'')

    tw_id = schema.TextLine(
        title=_(u'Twitter username'),
        description=_(u'example: @zestsoftware'),
        required=False,
        default=u'')

    default_img = schema.TextLine(
        title=_(u'Default image'),
        description=_(u'Path to default image'),
        required=False,
        default=u'/logo.png')

    default_img_width = schema.TextLine(
        title=_(u'Default image width'),
        description=_(u'The width of the default image expressed in pixel'),
        required=False,
        default=u'200')

    default_img_height = schema.TextLine(
        title=_(u'Default image height'),
        description=_(u'The hight of the default image expressed in pixel'),
        required=False,
        default=u'200')


class OGTagsCPForm(controlpanel.RegistryEditForm):
    schema = IOGTagsControlPanel
    label = _(u'OGTags settings')
    description = _(u'Settings for collective.ogtags')


class OGTagsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = OGTagsCPForm
