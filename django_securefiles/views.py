import os

from django.http import HttpResponse, Http404
from django.views import View

from .settings import SECUREFILES_PROTECTED_URL
from .utils import get_protected_file_path


class SecureFileView(View):
    """Generic secure file download view."""

    @staticmethod
    def has_permission(request, file_subpath):
        """Override this method to implement permission checks."""
        return request.user.is_authenticated

    @staticmethod
    def get_file_name(file_subpath):
        """Override if you want a nicer download filename."""
        return os.path.basename(file_subpath)

    def get(self, request, file_subpath):
        if not self.has_permission(request, file_subpath):
            raise Http404()

        protected_path = get_protected_file_path(file_subpath)

        if not os.path.exists(protected_path):
            raise Http404()

        response = HttpResponse()
        response['Content-Type'] = ''  # nginx will auto-detect
        response['X-Accel-Redirect'] = os.path.join(SECUREFILES_PROTECTED_URL, file_subpath)
        response['Content-Disposition'] = f'attachment; filename="{self.get_file_name(file_subpath)}"'
        return response
