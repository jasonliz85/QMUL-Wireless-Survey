
from django.contrib.auth            import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from django.template import Context, RequestContext, Template

from django.shortcuts import render_to_response

from models import Survey

@login_required
def index_view(request):
    context = RequestContext(request)
    return render_to_response("index.html", {"surveys": Survey.objects.all()}, context)

