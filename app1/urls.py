from django.urls import path
from app1.views import *

app_name='mi'
urlpatterns=[

path('rohit',rohit,name='rohit'),
path('rohit1/',rohit1,name='rohit1'),

]