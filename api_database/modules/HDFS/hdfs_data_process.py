# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : hdfs_data_process.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 13.
 * @comment  : HDFS 데이터 확인
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 13.  Ko Sun Ho       최초 작성
 *******************************************************************************
'''

import DocMinerAPI.settings as config
from hdfs import InsecureClient
import pandas as pd

class HDFS():
    def __init__(self,file_name):
        self.client_hdfs = InsecureClient('http://hmng1:17777')
        self.file_name = file_name

    def get_data_hdfs_main(self):
        with self.client_hdfs.read(self.file_name, encoding='utf-8') as reader:
            df = pd.read_csv(reader, index_col=0)
        return df

    def get_data_hdfs_main_txt(self):
        res = []
        with self.client_hdfs.read(self.file_name,encoding='utf-8') as reader:
            for line in reader:
                print(line)
                res.append(line)
        return res

if __name__ == '__main__':
    # filename = '/1.hdfs_test/new_20220408.txt'
    filename = '/hdfs_test/helloworld.csv'
    ins_hdfs = HDFS(file_name=filename)

    # res = ins_hdfs.get_data_hdfs_main_txt()
    res = ins_hdfs.get_data_hdfs_main()
    print(res)





