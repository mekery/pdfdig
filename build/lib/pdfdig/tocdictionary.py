'''
@summary: TOCDictionary class file.
          Construct TOC dictionary object from dictionary json file.

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: tocdictionary.py 2012-03-31 Micle Bu
'''
import json
import os
import sys

__all__ = ['TOCDictionary']

class TOCDictionary():
    def __init__(self, path, threshold=0.05):
        self.path = path
        self.threshold = threshold
        self.dictionary = dict()
        
    def build(self):
        """
        Build dictionary for TOC construction.
        The probability of a dictionary item can be computed using p=frequency/total.
        The items with probability p < THRESHOLD will be ignored in output.
        """
        json_file_dictionary = os.path.join(self.path, 'dictionary.json')
        json_file_articles = os.path.join(self.path, 'articles.json')        
        
        try:
            a_file = open(json_file_articles)
            d_file = open(json_file_dictionary)
            json_string_articles = a_file.read()
            json_string_dictionary = d_file.read()
        except: 
            print >>sys.stderr, ('\nERROR: There are something wrong with the toc dictionary path. ' 
                                 'Please check if json files exist in {0}\n'
                                 'You may specify the toc dictionary path using the -d/-p option. \n'
                                 'Use -h/--help option for details.'.format(self.path))
            exit()
            
        articles = json.loads(json_string_articles)
        dictionary = json.loads(json_string_dictionary)
        
        # build dictionary
        total = len(articles)
        for k,v in sorted(dictionary.items(), key=lambda x:x[1], reverse=True):
            if (1.0*v)/total > self.threshold:
                self.dictionary[k]=v 
        
        a_file.close()
        d_file.close()
        
        return self.dictionary
        
            

        
        
        