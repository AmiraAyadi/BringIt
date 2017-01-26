from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^enregistrement/', views.enregistrement, name='enregistrement'),

]
