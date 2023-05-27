from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

  path('',views.home,name='home'),
  path('login/',views.login,name='login'),
  path('signin/',views.signin,name='signin'),
  path('forgot_password/',views.forgot_password,name='forgot_password'),
  path('change_password/',views.change_password,name='change_password'),
  path('otp/',views.otp,name='otp'),
  path('logout/',views.logout,name='logout'),
  path('htmlcontent/<slug:status>',views.htmlcontent,name='htmlcontent'),
  path('htmlquestions/',views.htmlquestions,name='htmlquestions'),
  path('payment/<slug:corse>',views.payment,name='payment'),
  path('feedback/<slug:status>',views.feedback,name='feedback'),
  path('savecode/',views.savecode,name='savecode'),
  path('filesave/',views.filesave,name='filesave'),
  path('searchfile/',views.searchfile,name='searchfile'),
  path('renamefile/',views.renamefile,name='renamefile'),
  path('openfile/',views.openfile,name='openfile'),
  path('doubt/<slug:status>',views.doubt,name='doubt'),
  path('htmlex/<num>',views.htmlex,name='htmlex'),
  path('premium/<slug:name>',views.premium,name='premium'),

]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)