'''
@summary: MatchLite class file, pattern matching

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: pdfmatch.py 2012-04-22 Micle Bu
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