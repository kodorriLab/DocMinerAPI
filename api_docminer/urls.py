#-*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : api_docminer/urls.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 08.
 * @comment  : api_docminer 모듈 URL 경로 설정
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 08.  Ko Sun Ho    최초 작성
 *******************************************************************************
'''

from django.urls import path
from . import views # views.py 파일 불러옴

urlpatterns = [
    path('docminerview/', views.DocMinerView.as_view(), name='docminerview') # views 파일에서 DocMinerView class 호출
]