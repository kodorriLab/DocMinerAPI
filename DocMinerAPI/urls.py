#-*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : urls.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 16.
 * @comment  : DocMinerAPI 장고 프레임워크 REST API URL 경로 설정
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 16.  Ko Sun Ho    최초 작성
 *******************************************************************************
'''

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api_sharing.views import HomeView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path(r'', HomeView.as_view(), name='home'),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api_docminer/', include('api_docminer.urls')),
    path(r'api_database/', include('api_database.urls')),
]



