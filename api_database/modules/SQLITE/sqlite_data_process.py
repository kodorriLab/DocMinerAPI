# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : sqlite_data_process.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 15.
 * @comment  : django 기본 db sqlite 처리 테스트 용 스크립트
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 15.  Ko Sun Ho       최초 작성
 *******************************************************************************
'''

import sqlite3
from DocMinerAPI.settings import BASE_DIR, SQLITE_CONFIG_DEV
import logging

log = logging.getLogger(__name__)

class SQLITE:

    def __init__(self):
        self.conn = sqlite3.connect(str(BASE_DIR) + '/db.sqlite3')
        self.cur = self.conn.cursor()

    def insert_data_sqlite(self, data):
        # data -> [file_name, text]
        table = SQLITE_CONFIG_DEV['table']['test']
        print(table)
        sql = "insert into {}(file_name,text) values (?, ?)".format(table)

        try:
            self.cur.executemany(sql, [data])
            self.conn.commit()  # 트랜잭션 내용 DB 반영

        except self.conn.Error as e:
            log.info("sqlite3 insert error - {}".format(e))
            print("sqlite3 insert error - {}".format(e))
            if self.conn:
                self.conn.rollback() # DB 반영 X 트랜잭션 이전 상태로 되돌림

        write_path = str(BASE_DIR) + '/static/txt/' + data[0] + '.txt'
        with open(write_path, 'w', encoding='utf-8') as file:
            file.write(data[1])

        return {'write_path': write_path}

if __name__ == '__main__':
    ins_sqlite = SQLITE()
    data = ['file_name_test','bbb_text_test']
    r = ins_sqlite.insert_data_sqlite(data=data)
    print('000000')
    print(r)
