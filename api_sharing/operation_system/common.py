# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * @fileName : common.py
 * @author   : "Ko Sun Ho"
 * @comment  : 문서 파일 가져오기 함수
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 05. 16.  Ko Sun Ho       작성
 *******************************************************************************
'''
import os
import sys

class OperatingSystem:

    # 현재 디레토리를 확인.
    @staticmethod
    def this_dir():
        return os.getcwd() + "/"

    # 해당 경로 디렉토리 내 모든 파일을 확인.
    @staticmethod
    def check_files(check_dir):
        fileNames = []
        for root, dirs, files in os.walk(check_dir):
            for file in files:
                fileNames.append(file.strip())
        return fileNames

    # 해당 경로 부모 디렉토리 가져오기
    @staticmethod
    def get_parent_path(check_dir):
        return os.path.abspath(os.path.join(check_dir, os.pardir))

    # 파일 확장자별 filename dic 생성 ex) ('pdf':[sample.pdf],'docx':[sample.docx])
    @staticmethod
    def separate_file_extension(check_dir):
        fileNames = OperatingSystem.check_files(check_dir)
        file_extension_dic = dict()
        for file in fileNames:
            temp = file.split('.')
            if temp[1] in file_extension_dic.keys():
                file_extension_dic[temp[1]].append(temp[0])
            else:
                file_extension_dic[temp[1]] = [temp[0]]
        return file_extension_dic

    # [파일명, 확장자] list 생성
    @staticmethod
    def separate_file_format_list(check_dir):
        fileNames = OperatingSystem.check_files(check_dir)
        res = []
        for file in fileNames:
            f_name,ext = os.path.splitext(file)
            temp = (f_name,ext)
            res.append(temp)
        return res

    @staticmethod
    def make_dir(check_dir):
        try:
            if not os.path.exists(check_dir):
                os.makedirs(check_dir)
        except OSError:
            print('Error: Creating dir -> {}'.format(check_dir))


def write_txt_file(save_path, save_name, text):
    # save path 체크 *없을시 생성
    OperatingSystem.make_dir(os.path.join(save_path))
    with open(os.path.join(save_path, save_name + '.txt'), 'w',encoding='utf8') as f:
        f.write(text)
