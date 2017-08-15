from django.conf.urls import url
from cruiseWeb import views

app_name = 'cruiseWeb'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^project', views.projectDescr, name='projectDescription'),
    url(r'^aboutUs', views.aboutUs, name = 'aboutUs'),
    url(r'^survey', views.gtSurvey, name = 'gtSurvey'),
    url(r'^cruiseMock', views.cruiseDemo, name='cruiseDemo'),
    url(r'^technical', views.technicalElement, name='technical'),
    url(r'^thanks', views.thankyou, name='thankyou'),
]
