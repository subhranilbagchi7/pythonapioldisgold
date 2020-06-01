from api.getapi import abc
from rest_framework import routers
router=routers.DefaultRouter()
router.register('SignupPage',abc)