from django.conf.urls import include, url
from blog import views

urlpatterns = [
    # Examples:
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^register/$', 'blog.views.register', name='register'), 
    
    url(r'^categories/(?P<categoryslug>.*)/$', 'blog.views.category'),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    #url(r'^search-form/$', views.search_form),
    #url(r'^search/$', views.search),
]
