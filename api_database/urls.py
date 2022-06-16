#-*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : api_database/urls.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 13.
 * @comment  : api_database 모듈 URL 경로 설정
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 13.  Ko Sun Ho    최초 작성
 *******************************************************************************
'''

from django.urls import path
from . import views # views.py 파일 불러옴

urlpatterns = [
    path('hdfsview/', views.HDFSView.as_view(), name='hdfsview'), # views 파일에서 DocMinerView class 호출
    # path('sqliteview/', views.HDFSView.as_view(), name='sqliteview')
]