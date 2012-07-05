'''
Created on Mar 29, 2012

@author: micle
'''
import unittest
from pdfdig.pdftext import Text

## TestCase
#class NormalizeTestCase(unittest.TestCase):
#    def setUp(self):
#        pdf = '../example/sample.pdf'
#        self.text = Text(pdf)
#    def tearDown(self):
#        self.text = None
#    def testNormalize(self):
#        print self.text.normalize()
#
## Test
#if __name__ == '__main__':
#    suite = unittest.TestSuite()
#    suite.addTest(NormalizeTestCase('testNormalize'))
#    
#    runner = unittest.TextTestRunner()
#    runner.run(suite)

pdf = '../example/coordinate.pdf'
text = Text(pdf)

#pages =
#print text.pagecount 

pages = text.pages

print len(pages)
#print pages[10]

lines = text.getlines()
for line in lines:
    print 'p:{0}\tn:{1}\tc:{2}'.format(line[0],line[1],line[2])

