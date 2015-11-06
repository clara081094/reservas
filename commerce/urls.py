from django.conf.urls import patterns, include, url

from commerce import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.ingresar, name='ingresar'),
  	
    )