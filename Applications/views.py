from django.http import HttpResponse
from .models import windowsApp

def index(request):
    all_windowsApp = windowsApp.objects.all()
    html = ''
    for test in all_windowsApp:
        url = '/Applications/' + str(test.id) + '/'
        html += '<a href = "' + url + '">' + test.username + '</a><br>'
    return HttpResponse(html)

def detail(request,windowsApp_id):
    return HttpResponse("<h2> Details for Apps: " + str(windowsApp_id) +"</h2>")