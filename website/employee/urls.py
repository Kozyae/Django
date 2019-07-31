from django.conf.urls import url
from .import views

app_name = 'employee'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /employee/sick/
    url(r'sick/$', views.Index2View.as_view(), name='index2'),
    #   /employee/sick/1/
    url(r'sick/(?P<pk>[0-9]+)/$', views.DetailsickView.as_view(), name='detail_sick'),

    # /employee/annual/
    url(r'annual/$', views.Index3View.as_view(), name='index3'),
    #  /employee/annual/1/
    url(r'annual/(?P<pk>[0-9]+)/$', views.DetailannualView.as_view(), name='detail_annual'),

    # /employee/unpay/
    url(r'unpay/$', views.Index4View.as_view(), name='index4'),
    #  /employee/unpay/1/
    url(r'unpay/(?P<pk>[0-9]+)/$', views.DetailunpayView.as_view(), name='detail_unpay'),



    # /employee/album/add/
    url(r'employee/add/$', views.Employeecreate.as_view(), name='employee-add'),
    # /employee/sick/add/
    url(r'sick/add/$', views.Sickcreatesick.as_view(), name='sick-add'),
    # /employee/annual/add/
    url(r'annual/add/$', views.Annualcreatesick.as_view(), name='annual-add'),
    # /employee/unpay/add/
    url(r'unpay/add/$', views.Unpaycreatesick.as_view(), name='unpay-add'),

    #/employee/employee/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.Employeeupdate.as_view(), name='employee-update'),
    #/employee/sick/update
    url(r'sick/(?P<pk>[0-9]+)/update/$', views.Sickupdatesick.as_view(), name='sick-update'),
    #/employee/annual/update
    url(r'annual(?P<pk>[0-9]+)/update/$', views.Annualupdateannual.as_view(), name='annual-update'),
    #/employee/unpay/update
    url(r'unpay(?P<pk>[0-9]+)/update/$', views.Unpayupdateunpay.as_view(), name='unpay-update'),



    # /employee/employee/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.Employeedelete.as_view(), name='employee-delete'),


    # /employee/employee/2/delete/
    url(r'sick/(?P<pk>[0-9]+)/delete/$', views.Sickdelete.as_view(), name='sick-delete'),

    # /employee/employee/2/delete/
    url(r'annual/(?P<pk>[0-9]+)/delete/$', views.Annualdelete.as_view(), name='annual-delete'),


    # /employee/employee/2/delete/
    url(r'unpay/(?P<pk>[0-9]+)/delete/$', views.Unpaydelete.as_view(), name='unpay-delete'),



]