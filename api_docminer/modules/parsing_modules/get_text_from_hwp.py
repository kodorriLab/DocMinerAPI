# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * @fileName : get_text_from_hwp.py
 * @author   : "Ko Sun Ho"
 * @comment  : 문서 파싱 hwp module (lib - olefile)
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 05. 16.  Ko Sun Ho       작성
 *******************************************************************************
'''
import os
import olefile
import zlib
import struct


class GetHwpText:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename
        self.fullpath = self.filepath + '/' + self.filename + '.hwp'
        self.f = olefile.OleFileIO(self.fullpath)
        self.dirs = self.f.listdir()
        # HWP 파일 검증
        if ["FileHeader"] not in self.dirs or \
                ["\x05HwpSummaryInformation"] not in self.dirs:
            raise Exception("Not Valid HWP.")

    def _get_word_text(self):
        # 문서 포맷 압축 여부 확인
        header = self.f.openstream("FileHeader")
        header_data = header.read()
        is_compressed = (header_data[36] & 1) == 1

        # Body Sections 불러오기
        nums = []
        for d in self.dirs:
            if d[0] == "BodyText":
                nums.append(int(d[1][len("Section"):]))
        sections = ["BodyText/Section" + str(x) for x in sorted(nums)]

        # 전체 text 추출
        text = ""
        for section in sections:
            bodytext = self.f.openstream(section)
            data = bodytext.read()
            if is_compressed:
                unpacked_data = zlib.decompress(data, -15)
            else:
                unpacked_data = data

            # 각 Section 내 text 추출
            section_text = ""
            i = 0
            size = len(unpacked_data)
            while i < size:
                header = struct.unpack_from("<I", unpacked_data, i)[0]
                rec_type = header & 0x3ff
                rec_len = (header >> 20) & 0xfff

                if rec_type in [67]:
                    rec_data = unpacked_data[i + 4:i + 4 + rec_len]
                    section_text += rec_data.decode('utf-16')
                    section_text += "\n"

                i += 4 + rec_len

            text += section_text
            text += "\n"

        return text

    def get_text_hwp_main_str(self):
        return self._get_word_text()

    def get_text_hwp_main_list(self):
        text = self._get_word_text()
        return text.split('\r\n')

    def get_text_hwp_main_with_filename(self):
        return [self.filename, self._get_word_text()]


if __name__ == '__main__':
    from doc_miner.common_modules.common import *

    # resources 경로가져오기
    fm = 'hwp'
    path = os.getcwd()
    rsc_path = OperatingSystem.get_parent_path(path)
    sample_path = os.path.join(rsc_path, 'resources/sample_doc')
    docx_files = OperatingSystem.sperate_file_extension(check_dir=sample_path)[fm]

    # .docx text 파싱
    sample_docx_filename = docx_files[0]
    ins_hwp = GetHwpText(filepath=sample_path, filename=sample_docx_filename)

    res_list = ins_hwp.get_text_hwp_main_list()
    print(res_list)

    res_str = ins_hwp.get_text_hwp_main_str()
    print(res_str)
