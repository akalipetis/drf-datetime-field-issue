from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'drf_datetime_field_issue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('simple_app.urls')),
]
