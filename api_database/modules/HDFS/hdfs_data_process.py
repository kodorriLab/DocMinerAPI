# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : hdfs_data_process.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 13.
 * @comment  : HDFS 데이터 관련 모듈
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 13.  Ko Sun Ho       최초 작성
 *******************************************************************************
'''

from DocMinerAPI.settings import *
from hdfs import InsecureClient
import pandas as pd

import logging
log = logging.getLogger(__name__)

class HDFS():
    def __init__(self):
        self.client_hdfs = InsecureClient(HDFS_CONFIG_PROD['con']['client'])

    def get_data_hdfs_main(self,file_name):
        with self.client_hdfs.read(file_name, encoding='utf-8') as reader:
            df = pd.read_csv(reader, index_col=0)
        return df

    def get_data_hdfs_txt_main(self,file_name):
        res = []
        with self.client_hdfs.read(file_name,encoding='utf-8') as reader:
            for line in reader:
                print(line)
                res.append(line)
        return res

    def write_data_hdfs_txt_main(self, data_li, format_):
        ''' data_li : [self.filename, self._get_word_text_str()] '''
        file_name = data_li[0].replace(' ','_')
        text = data_li[1]

        wr_path = HDFS_CONFIG_PROD['con']['write_bas_path'] + file_name + '/' + file_name + '_' + format_ +'.txt'
        try:
            with self.client_hdfs.write(wr_path) as writer:
                writer.write(text.encode())
                res = ['success',file_name, wr_path]
            log.info('hdfs write ==> path : {}'.format(wr_path))
        except Exception as e:
            msg = 'hdfs write err ==> {}'.format(e)
            log.info('hdfs write err ==> {}'.format(e))
            res = ['error',file_name,msg]
        return res



if __name__ == '__main__':
    # filename = '/1.hdfs_test/new_20220408.txt'
    filename = '/hdfs_test/helloworld.csv'
    ins_hdfs = HDFS(file_name=filename)

    # res = ins_hdfs.get_data_hdfs_main_txt()
    res = ins_hdfs.get_data_hdfs_main()
    print(res)





