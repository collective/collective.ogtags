from .controlpanel import IOGTagsControlPanel
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from plone.app.imaging.utils import getAllowedSizes


class OGTagsViewlet(ViewletBase):
    def meta_tags(self):
        self.settings = getUtility(IRegistry).forInterface(IOGTagsControlPanel)
        if not self.settings.enabled:
            return
        context = self.context.aq_inner
        tags = {}

        # set title
        title = context.title
        if title:
            tags['og:title'] = title
            tags['twitter:title'] = title

        # set description
        description = context.Description()
        if description:
            tags['og:description'] = description
            tags['twitter:description'] = description

        # set url
        url = context.absolute_url()
        if url:
            tags['og:url'] = url

        # social media specific
        if self.settings.fb_id:
            tags['fb:app_id'] = self.settings.fb_id
        if self.settings.fb_username:
            tags['og:article:publisher'] = "https://www.facebook.com/" \
                + self.settings.fb_username
        if self.settings.tw_id:
            tags['twitter:site'] = self.settings.tw_id
        tags['twitter:card'] = u'summary'

        # misc
        tags['og:type'] = u'website'
        if self.settings.og_site_name:
            tags['og:site_name'] = self.settings.og_site_name

        return tags

    def image_tags(self):
        self.settings = getUtility(IRegistry).forInterface(IOGTagsControlPanel)
        if not self.settings.enabled:
            return
        tags = []
        context = self.context.aq_inner
        try:
            scales = context.restrictedTraverse('/'.join(context.getPhysicalPath()) +'/@@images')
        except AttributeError:
            return
        if not scales:
            return
        try:
            field = context.getField('image') or context.getField('leadImage')
            if not field:
                raise AttributeError
        except:
            return
        for scale in [
                'og_fbl',
                'og_fb',
                'og_tw',
                'og_ln']:
            try:
                image = scales.scale(field.getName(), scale=scale)
                if not image:
                    continue
            except AttributeError:
                continue
            tag = {}
            if scale == 'og_tw':
                tag['twitter:image'] = image.url
            else:
                tag['og:image'] = image.url
                tag['og:image:width'] = image.width
                tag['og:image:height'] = image.height
            tags.append(tag.copy())
        return tags
