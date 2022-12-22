from django.core.exceptions import PermissionDenied

class adminRequired():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif not request.user.es_admin and  not request.user.is_superuser:
            raise PermissionDenied
        return super(adminRequired, self).dispatch(request, *args, **kwargs)
        


