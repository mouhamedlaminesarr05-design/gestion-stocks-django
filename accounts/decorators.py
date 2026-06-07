from django.core.exceptions import PermissionDenied


def role_required(*roles):
    """
    Vérifie que l'utilisateur appartient à l'un des rôles donnés.
    Exemple d'utilisation : @role_required('Responsable Stock')
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user_groups = request.user.groups.values_list('name', flat=True)
            if request.user.is_superuser or any(role in user_groups for role in roles):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator