from django.http import HttpResponse


def set_session(request):
    """
    Гейт для простановки в куки сессии
    :param request:
    :return:
    """
    session_id = request.GET.get('session')
    csrf = request.COOKIES.get('csrftoken')

    message = 'Set Cookie!' if session_id and csrf else 'Error!'
    response = HttpResponse(message)
    response.set_cookie('sessionid', session_id)
    response.set_cookie('csrftoken', csrf)
    return response
