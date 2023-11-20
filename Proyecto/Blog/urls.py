from django.urls import path
from Blog.views import *

urlpatterns = [
    path('', inicio, name="home"),
    path('postearForm/', postearForm, name='postearform'),
    
]
