import os

from django.http import Http404
from django.http import HttpResponse
from django.views import View

from fms import settings


class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        template_dir_path = settings.TEMPLATES[0]["DIRS"][0]
        final_path = os.path.join(template_dir_path, item + ".html")
        try:
            html = open(final_path)
            return HttpResponse(html)
        except:
            raise Http404
