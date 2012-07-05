PDFDig Tutorial
===============
This tutorial serves as the quick start for PDFDig.

Prerequisites
-------------
Python
^^^^^^
PDFDig is written in Python, so you should prepare Python environment first. Both Python 2 and Python 3 are OK.

Download Python from: 
 - http://www.python.org/getit/

Since PDFDig only provides Command Line Interface(CLI) utilities currently, we strongly recommand Windows users to use `Cygwin
<http://www.cygwin.com/>`_, a linux-like environment for Windows, as running environment for PDFDig to get full features of PDFDig.

Cygwin
^^^^^^
`Installing Cygwin
<http://cygwin.com/install.html>`_ is pretty easy and straightforward. 
 
 - Download `setup.exe
   <http://cygwin.com/setup.exe>`_.
 - Run setup.exe and follow its navigation.
 - When setup.exe asks you to **Select Packages**, make sure you have selected **Python Default** and then **python: Python language interpreter**.
 - After installation, you may try *python --version* within Cygwin Terminal.

pdftotext
^^^^^^^^^
PDFDig does not extract content from PDF documents directly by itself, but use a efficient utility, pdftotext, which is freely available and included by default with many Linux distributions. Xpdf provides a pdftotext port to Windows platform.

**Windows users:**
 - Download xpdf binaries, looks like **xpdfbin-win-3.03.zip**, from: http://www.foolabs.com/xpdf/download.html
 - Extract xpdfbin-win-3.03.zip in your favorite directory, take D:\\ as an example, you'll get D:\\xpdfbin-win-3.03.
 - pdftotext.exe locates in D:\\xpdfbin-win-3.03\\bin32\\ or D:\\xpdfbin-win-3.03\\bin64\\
 - Choose correct version of pdftotext depending on your system architecture, take 32-bit system as an example, you should use the pdftotext.exe in D:\\xpdfbin-win-3.03\\bin32\\.
 - Add pdftotext.exe directory **D:\\xpdfbin-win-3.03\\bin32\\** to PATH environment variable to ensure system can find pdftotext.exe.

**Unix/Linux users:** 

pdftotext is available and included by default with many Linux distributions. If pdftotext does not exsit in your system, install poppler-utils package.

**Check Test:**

You can test pdftotext, just run ::
  
  $ pdftotext -v
  Copyright 2005-2011 The Poppler Developers - http://poppler.freedesktop.org
  Copyright 1996-2004 Glyph & Cog, LLC

Installation
------------
1. Get PDFDig source, the tarball file looks like pdfdig-1.0.tar.bz2.
2. Extract the tarball file. 

::

  $ tar jxvf pdfdig-1.0.tar.bz2

3. Install PDFDig.

::
 
  $ cd pdfdig-1.0
  $ sudo python setup.py install

After the installation, PDFDig will copy PDFDig library to Python library and install 4 executable utilities in your system.

Utility
-------
PDFDig provides you 4 Command Line Interface(CLI) utilities, helps to process PDF documents and do the text processing in command line, so you may need a terminal in Unix/Linux or run `cmd` in Windows before using these utilities.

Refer to :doc:`utility` for details.
