from django.shortcuts import redirect


# Блокирует доступ неаутентифицированных пользователей
def unauthenticated_user(view_func):
    def wraper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shortener:index')
        else:
            return view_func(request, *args, **kwargs)
    return wraper_func
