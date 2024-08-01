from users.forms import AuthenticationAjaxForm, RegisterAjaxForm


def get_context_data(request):
    context = {
        'login_ajax': AuthenticationAjaxForm(),
        'registr_ajax': RegisterAjaxForm()
    }
    return context