# -*- coding: utf-8 -*-
'''
*******************************************************************************
 * @fileName : get_text_from_pdf.py
 * @author   : "Ko Sun Ho"
 * @comment  : 문서 파싱 pdf module (lib - pdfminer)
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 05. 16.  Ko Sun Ho       작성
 *******************************************************************************
'''
# import
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


class GetPdfText:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename
        self.fullpath = self.filepath + '/' + self.filename + '.pdf'
        self.f = open(self.fullpath, 'rb')
        self.output_string = StringIO()

    # full string return
    def _get_word_text_str(self):
        parser = PDFParser(self.f)
        doc = PDFDocument(parser)

        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, self.output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

        return str(self.output_string.getvalue())

    # list return(line)
    def _get_word_text_list(self):
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, self.output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        pages_text = []

        for page in PDFPage.get_pages(self.f):
            # Get (and store) the "cursor" position of stream before reading from PDF
            # On the first page, this will be zero
            read_position = self.output_string.tell()

            # Read PDF page, write text into stream
            interpreter.process_page(page)

            # Move the "cursor" to the position stored
            self.output_string.seek(read_position, 0)

            # Read the text (from the "cursor" to the end)
            page_text = self.output_string.read()
            a = page_text.split('\n\n')
            b = [i.replace('\n','') for i in a]

            # Add this page's text to a convenient list
            pages_text.extend(b)

        return pages_text

    def get_text_pdf_main_str(self):
        return self._get_word_text_str()

    def get_text_pdf_main_list(self):
        return self._get_word_text_list()

    def get_text_pdf_main_with_filename(self):
        return [self.filename, self._get_word_text_str()]


if __name__ == '__main__':
    from doc_miner.common_modules.common import *

    # resources 경로가져오기
    fm = 'pdf'
    path = os.getcwd()
    rsc_path = OperatingSystem.get_parent_path(path)
    sample_path = os.path.join(rsc_path, 'resources/sample_doc')
    docx_files = OperatingSystem.sperate_file_extension(check_dir=sample_path)[fm]

    # .docx text 파싱
    sample_docx_filename = docx_files[0]
    ins_pdf = GetPdfText(filepath=sample_path, filename=sample_docx_filename)

    res_list = ins_pdf.get_text_pdf_main_list()
    print(res_list)

    res_str = ins_pdf.get_text_pdf_main_str()
    print(res_str)
