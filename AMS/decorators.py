from django.shortcuts import redirect

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'student_id' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
