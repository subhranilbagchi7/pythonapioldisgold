
from django.conf.urls import url
from django.urls import path, include

from .abc import SignupPage, SignupPageUserDetails

urlpatterns = [

    url('ants/covid19api/SignUp/', SignupPage.as_view(), name='Signup'),
    url('ants/covid19api/(?P<passangers_id>\d+)', SignupPageUserDetails.as_view(), name='User_details')
]
