# -*- coding: utf-8 -*-
from cpskin.core.utils import safe_utf8
from plone import api
from plone.app.contenttypes.browser.file import FileView as BaseFileView


class FileView(BaseFileView):

    def __call__(self):
        context = self.context
        if api.user.is_anonymous():
            download_url = '{0}/@@download/file/{1}'.format(
                context.absolute_url(),
                safe_utf8(context.file.filename),
            )
            self.request.response.redirect(download_url)
            return ''
        return super(FileView, self).__call__()
