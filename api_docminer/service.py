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
from api_database.modules.LOCAL.local_data_process import *
import json
import logging

log = logging.getLogger(__name__)

def none_params_msg():
    return {"status":"error", "message": "the JSON object must be str, bytes or bytearray, not 'NoneType'"}

# 단순 text 추출
def get_data_from_doc(params):
    if params is None:
        return none_params_msg()
    else:
        #json 형식 변환
        json_loads = json.loads(params)

        # 입력받은 doc 경로
        doc_path = json_loads['doc_path']

        # 추출 텍스트 저장
        output = json_loads['output']

        # IP 확인
        ip_address = json_loads['IP']

        log.info("\n{} ::: ============ Docminer service START ============"
                 "\n{} ::: rsc_path => {}"
                 "\n{} ::: output => {}\n"
                 .format(ip_address,
                         ip_address,doc_path,
                         ip_address,output
                         ))

        # 해당경로 파일 리스트 추출
        docx_files = OperatingSystem.separate_file_format_list(check_dir=doc_path)

        res_dic = dict()
        for file in docx_files:
            file_name = file[0] # file 이름
            format_ = file[1].replace('.','') # file 확장자
            ins_service = DocMinerService(rsc_path=doc_path, file_name=file_name, format_=format_)

            # 확장자별 로직 분리
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

            if output == 'hadoop':
                pass
            elif output == 'local':
                ins_local = LOCAL(data_li=res)
                write_res = ins_local.write_data_local()
                res_dic[write_res[0] + '.' + format_] = write_res[1]
            else:
                raise Exception('please check output :: use only hadoop or local')

        return res_dic

# 텍스트 추출 + 분석 기법 추가
def get_data_analysis_from_doc(params):
    if params is None:
        return none_params_msg()
    else:
        pass







