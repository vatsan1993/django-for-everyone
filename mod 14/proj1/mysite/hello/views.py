
from django.http import HttpResponse

# Create your views here.
def myview(request):
    session_count = request.session.get("count", 0) + 1
    if session_count > 4:
        session_count = 1
    request.session['count'] = session_count
    response = HttpResponse("view count="+str(session_count) )
    response.set_cookie('dj4e_cookie', 'f5efd30f', max_age=1000)
    return response