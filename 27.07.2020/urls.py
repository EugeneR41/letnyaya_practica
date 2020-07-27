from django.conf.urls import url

from routing.views import simple_route, slug_route, sum_route, sum_get_method, sum_post_method

urlpatterns = [
    url(r'^routing/simple_route/$', simple_route),
    url(r'^routing/slug_route/([0-9a-z-_]{1,16})/$', slug_route),
    url(r'^/routing/sum_route/([-]?\d+)/([-]?\d+)/$', sum_route),
    url(r'^sum_get_method/$', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method),
]