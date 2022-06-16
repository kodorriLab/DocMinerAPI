# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : local_data_process.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 15.
 * @comment  : parse text local write 테스트 모듈
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 13.  Ko Sun Ho       최초 작성
 *******************************************************************************
'''

from DocMinerAPI.settings import BASE_DIR

class LOCAL():
    def __init__(self,data_li):
        self.file_name = data_li[0]
        self.parse_text = data_li[1]

    def write_data_local(self):
        write_path = str(BASE_DIR).replace('\\','/') + '/static/txt/' + self.file_name + '.txt'
        with open(write_path, 'w', encoding='utf-8') as file:
            file.write(self.parse_text)

        return [self.file_name, write_path]





