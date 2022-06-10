# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * Copyright ⓒ 2019 WIPS Co.,Ltd.
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : api_docminer/service.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 09.
 * @comment  : docminer 모듈 사용을 위한 비즈니스 로직 Service 분리
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 09.  Ko Sun Ho    최초 작성
 *******************************************************************************
'''

from api_sharing.operation_system.common import *
from api_docminer.modules.service_modules.docminer_service import *

def none_params_msg():
    return {"status":"error", "message": "the JSON object must be str, bytes or bytearray, not 'NoneType'"}

# 단순 text 추출
def get_data_from_doc(params):
    if params is None:
        return none_params_msg()
    else:
        rsc_path = params.get('rsc_path')
        output = params.get('output')
        docx_files = OperatingSystem.separate_file_format_list(check_dir=rsc_path)

        for file in docx_files:
            file_name = file[0] # file 이름
            format_ = file[1].replace('.','') # file 확장자
            ins_service = DocMinerService(rsc_path=rsc_path, file_name=file_name, format_=format_)

            if format_ == 'pdf':
                res = ins_service.get_text_from_pdf_with_filename()
            elif format_ == 'docx':
                res = ins_service.get_text_from_docx_with_filename()
            elif format_ == 'hwp':
                res = ins_service.get_text_from_hwp_with_filename()
            elif format_ == 'pptx':
                res = ins_service.get_text_from_pptx_with_filename()
            else:
                raise Exception('please check file format')

            if output == 'txt':
                # write_txt_file(save_path=config.txt_save_path, save_name=res[0], text=res[1])
                pass
            elif output == 'hadoop':
                pass

# 텍스트 추출 + 분석 기법 추가
def get_data_analysis_from_doc(params):
    if params is None:
        return none_params_msg()
    else:
        pass







