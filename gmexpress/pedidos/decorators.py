from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff or user.groups.filter(name__iexact='Admin').exists()

def is_chofer(user):
    return user.groups.filter(name__iexact='Chofer').exists()

def admin_required(view_func):
    decorated = user_passes_test(is_admin, login_url='login')(view_func)
    return decorated

def chofer_required(view_func):
    decorated = user_passes_test(is_chofer, login_url='login')(view_func)
    return decorated
