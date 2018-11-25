from django.conf.urls import include, url
from django.contrib import admin
from teacherr import views as tv
from teacherr import teacher_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),
    url(r'^teacher/', include(teacher_url)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),
    url(r'^yourname/$', tv.do_extemParam, {"name":"计益成"}),
    url(r'^mayiknowyourname/$', tv.recParse, name="askname"),
]
