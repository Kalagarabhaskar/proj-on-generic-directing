from django.urls import path
from app2.views import *

app_name='gt'
urlpatterns=[

path('sky',sky,name='sky'),
path('sky1/',sky1,name='sky1'),

]