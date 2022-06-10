# -*- coding: utf-8 -*-
"""
*******************************************************************************
 * @fileName : docminer_service.py
 * @author   : "Ko Sun Ho"
 * @comment  : 문서 파싱 비즈니스 로직 분리
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 05. 20.  Ko Sun Ho       작성
 *******************************************************************************
"""

from api_docminer.modules.parsing_modules.get_text_from_pdf import *
from api_docminer.modules.parsing_modules.get_text_from_docx import *
from api_docminer.modules.parsing_modules.get_text_from_hwp import *
from api_docminer.modules.parsing_modules.get_text_from_pptx import *


class DocMinerService:

    def __init__(self, rsc_path, file_name, format_):
        # 문서 파일 있는 resource 디렉토리 경로
        self.rsc_path = rsc_path
        self.file_name = file_name
        if format_ == 'pdf':
            self.ins_pdf = GetPdfText(filepath=self.rsc_path, filename=self.file_name)
        elif format_ == 'docx':
            self.ins_docx = GetDocxText(filepath=self.rsc_path, filename=self.file_name)
        elif format_ == 'hwp':
            self.ins_hwp = GetHwpText(filepath=self.rsc_path, filename=self.file_name)
        elif format_ == 'pptx':
            self.ins_pptx = GetPptxText(filepath=self.rsc_path, filename=self.file_name)
        else:
            raise Exception('please check format')

    ##########################################################
    # full string 추출
    def get_text_from_pdf_full_str(self):
        res_str = self.ins_pdf.get_text_pdf_main_str()
        return res_str

    def get_text_from_docx_full_str(self):
        res_str = self.ins_docx.get_text_docx_main_str()
        return res_str

    def get_text_from_hwp_full_str(self):
        res_str = self.ins_hwp.get_text_hwp_main_str()
        return res_str

    def get_text_from_pptx_full_str(self):
        res_str = self.ins_pptx.get_text_pptx_main_str()
        return res_str

    ##########################################################
    # list 추출
    def get_text_from_pdf_full_list(self):
        res_list = self.ins_pdf.get_text_pdf_main_list()
        return res_list

    def get_text_from_docx_full_list(self):
        res_list = self.ins_docx.get_text_docx_main_list()
        return res_list

    def get_text_from_hwp_full_list(self):
        res_list = self.ins_hwp.get_text_hwp_main_list()
        return res_list

    def get_text_from_pptx_full_list(self):
        res_list = self.ins_pptx.get_text_pptx_main_list()
        return res_list

    ##########################################################
    # 리스트 추출 [file_name, full string]
    def get_text_from_pdf_with_filename(self):
        res = self.ins_pdf.get_text_pdf_main_with_filename()
        return res

    def get_text_from_docx_with_filename(self):
        res = self.ins_docx.get_text_docx_main_with_filename()
        return res

    def get_text_from_hwp_with_filename(self):
        res = self.ins_hwp.get_text_hwp_main_with_filename()
        return res

    def get_text_from_pptx_with_filename(self):
        res = self.ins_pptx.get_text_pptx_main_with_filename()
        return res
