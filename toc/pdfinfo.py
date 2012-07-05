#coding=utf-8
'''
Created on Mar 31, 2012

@author: micle
'''
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfdig.normalizer import normalize_title, normalize_toc_item

__all__ = ['Info']

class Info():
    def __init__(self, pdf):
        self.pdf = pdf
        self.title = ''
        self.toc = self.get_toc()
    
    def get_toc(self):
        fp = open(self.pdf, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        
        # title
        if doc.info:
            metadict = doc.info[0]
            if 'Title' in metadict.keys():
                self.title = normalize_title(metadict['Title'])

        # level 1 of toc
        try:
            outlines = doc.get_outlines()
            toc = list()
            select_level = self.get_level1(outlines)
        except:
            return None
        for (level,title,dest,a,se) in doc.get_outlines():
            if level==select_level:
                toc.append(normalize_toc_item(title))
        return toc
    
    def get_level1(self, outlines):
        count = 0
        first = ''
        for (level,title,dest,a,se) in outlines:
            if count == 0:
                first=title
            if level == 1:
                count += 1
        
        if count == 1:
            return 2
        else:
            return 1