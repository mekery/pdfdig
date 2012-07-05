## PDFDig Introduction

PDFDig is a useful tool to dig content from pdf document for text mining, which is written in Python and based on pdftotext and PDFMiner.

* Home: https://github.com/mekery/pdfdig
* Documentation: http://mekery.github.com/pdfdig/

### Features ###

* Convert pdf to txt.
* Search in pdf document, working like grep.
* Build table of content(TOC) of pdf document.
* Get pdf metadata.

## PDFDig Utility

### pdftotext.py ###

pdftotext.py converts pdf to text. There are tens of similar utilities can do this job, while few of them, including pdftotext, can process line-break, hyphen and extra white spaces appropriately, and some of them render the pdf in physical order, which are unsuitable for multi-column pdf documents.

pdftotext.py uses pdftotext to get the text content of pdf document, then normalizes the text content.

### pdfgrep.py ###

pdfgrep.py enables you to search and count in pdf files. pdfgrep.py searches in grep-style, which means you can use regular expression in search and get matching lines.

## Reference ##

* pdftotext: http://en.wikipedia.org/wiki/Pdftotext
* PDFMiner: http://www.unixuser.org/~euske/python/pdfminer/