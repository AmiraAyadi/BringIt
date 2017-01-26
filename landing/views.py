from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
#page d'accueil :
def accueil(request):
    return render_to_response('accueil.html')
