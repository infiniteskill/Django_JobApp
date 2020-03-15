from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="jobhome"),
    path('contact', views.contact,name="contact"),
    path('postjob', views.postjob,name="postjob"),
    path('custom', views.customfilter,name="custom"),
    path('autodelete', views.autdelete,name="autodelete"),
    
    
]

