from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    #url(r'^about/$', 'app.views.aboutus', name='home'),
    #url(r'^bussiness/$', 'app.views.bussiness', name='home'),
    #url(r'^tech/$', 'app.views.Technology', name='home'),
    #url(r'^outsource/$', 'app.views.outsource', name='home'),
    url(r'^careers/$', 'careers.views.careers', name='home'),
    url(r'^fresher/$', 'careers.views.fresher', name='home'),
    url(r'^exp/$', 'careers.views.Experience', name='home'),
    #url(r'^why ampm/$', 'app.views.Why_AMPM', name='home'),
    url(r'^walkin/$', 'careers.views.Walkin', name='home'),
    url(r'^register/$', 'careers.views.register', name='home'),
    url(r'^forgotpwd/$', 'careers.views.forgotpwd', name='home'),
    url(r'^profile/$', 'careers.views.profile', name='home'),
    url(r'^logout/$', 'careers.views.logout_view',name='logout_page'),
    url(r'^success/$', 'careers.views.success',name='logout_page'),
    url(r'^upcomming/$', 'careers.views.upcomming_open',name='logout_page'),
    url(r'^resetpwd/(?P<uid>\d+)$', 'careers.views.resetpwd',name='resetpwd'),
    #url(r'^details/$', 'app.views.get_details',name='logout_page'),
    #url(r'^list/$', 'app.views.listing',name='logout_page'),
    #url(r'^data/(?P<id>\d+)/$', 'app.views.user_details',name='logout_page'),
    url(r'^map/$', 'contact.views.google_map',name='google_map'),
    url(r'^facebook/$', 'careers.views.facebook',name='facebook'),
    url(r'^google/$', 'careers.views.google',name='google'),
    url(r'^linkedin/$', 'careers.views.linkedin',name='linkedin'),
    url(r'^youtube/$', 'careers.views.youtube',name='youtube'),
    url(r'^twitter/$', 'careers.views.twitter',name='twitter'),
    url(r'^expprofile/$', 'careers.views.Exp_Profile',name='Exp_Profile'),
    #url(r'^contact/$', 'app.views.contact',name='contact'),
    url(r'^india/$', 'contact.views.india',name='india'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^editprofilepic/$', 'careers.views.editprofilepic', name='editprofilepic'),
    url(r'^terms/$', 'home.views.Terms_Conditions',name='Terms_Conditions'),
    url(r'^positions/$', 'careers.views.Current_positions',name='Current_positions'),
    url(r'^python/$', 'careers.views.python',name='python'),
     url(r'^list/$', 'careers..views.data',name='Terms_Conditions'),
    url(r'^show/$', 'careers..views.show',name='Terms_Conditions'),
    url(r'^service/$', 'services.views.services',name='service'),
  

  

    url(r'^admin/', include(admin.site.urls)),
)


