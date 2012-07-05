'''
Created on Apr 22, 2012

@author: micle
'''
from pdfdig.pdfmatch import Match

class MatchLite(Match):
    def __init__(self, pattern, pdffile, lines, icase=False, location=False, 
                 context=0, dictionary=None):        
        self.pattern = pattern
        self.file = pdffile
        self.icase = icase
        self.location= location
        self.context = context
        self.dictionary = dictionary
        self.lines = lines
                
        # result
        self.count = 0
        self.matches = self.domatch()