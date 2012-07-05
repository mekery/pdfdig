PDFDig Utility
==============
PDFDig provides you 4 Command Line Interface(CLI) utilities, helps to process PDF documents and do the text processing in command line, so you may need a terminal in Unix/Linux or run `cmd` in Windows before using these utilities.

1. pdftotext.py
---------------
pdftotext.py converts pdf to text. There are tens of similar utilities can do this job, while few of them, including pdftotext, can process line-break, hyphen and extra white spaces appropriately, and some of them render the pdf in physical order, which are unsuitable for multi-column pdf documents.

pdftotext.py uses pdftotext to get the text content of pdf document, then normalizes the text content.

Usage
^^^^^
::

  $ pdftotext.py [options] filename1 ...
  
The :program:`pdftotext.py` script has several options:

.. program:: pdftotext.py

.. option:: -o, --output OUTPUTFILE

   Specify the output file. e.g: output.txt

.. option:: -y, --layout LAYOUT

   Maintain the layout of the text. LAYOUT can be:
   
   **raw** 
     keep the text in content stream order. This is the default setting.
   
   **layout**
     preserve the original physical layout of the text.

.. option:: -f, --first-page INT
   
   First page to convert.
   
.. option:: -l, --last-page INT

   Last page to convert.
   
.. option:: -p, --page INT

   Specify a page to convert.

.. option:: -h, --help

   Print usage information.
   
Examples
^^^^^^^^
::

  $ pdftotext.py input.pdf
  $ pdftotext.py -o output.txt input.pdf

2. pdfgrep.py
-------------
pdfgrep.py enables you to search and count in pdf files. pdfgrep.py searches in grep-style, which means you can use regular expression in search and get matching lines.

Usage
^^^^^
::

  $ pdfgrep.py [options] pattern filename ...
  
The :program:`pdfgrep.py` script has several options:

.. program:: pdfgrep.py

.. option:: -o, --output OUTPUTFILE

   Specify the output file. e.g: output.txt

.. option:: -c, --count

   Print the number of matches for each input file, instead of normal ouput.

.. option:: -i, --ignore-case

   Ingnore case distinctions.

.. option:: -f, --file-prefix

   Prefix each line of output with input file.

.. option:: -p, --page-number

   Prefix each line of output with page number.

.. option:: -n, --line-number

   Prefix each line of output with 1-based line number within its txt file.

.. option:: -t, --context NUM

   Print at most NUM characters of context around each match. e.g: -t 100

.. option:: -d, --dictionary PATH

   Specify the TOC dictionary directory.
              
.. option:: -l, --location

   Print the match location within TOC.

.. option:: -C, --color COLOR

   Highlight color. COLOR is red by default, also can be black,red,green,orange,blue,purple,bluegreen or white.

.. option:: -h, --help

   Print usage information.
   
Examples
^^^^^^^^
::

  # search in pdf, support multi-pdf at once
  $ pdfgrep.py -in "keword" input1.pdf input2.pdf
  
  # search in directory  
  $ pdfgrep.py -in "keword" pdf-directory
  
  # search and count
  $ pdfgrep.py -c "keword" input.pdf
  
  # support location within TOC
  $ pdfgrep.py -nl -o output.txt input.pdf
  
  # change highlight color
  $ pdfgrep.py -C blue output.txt input.pdf
  
  # save results in a file with a name of output.txt, highlight doesn't work in this case
  $ pdfgrep.py -nl -o output.txt input.pdf

Output Formarts
^^^^^^^^^^^^^^^
The output of search results are formatted to make it more readable. For example, run
::

  $ pdfgrep.py -inf  "brain" input.pdf

The output may look like:
::

  @F:input.pdf @N: 335	 @C:  Longitudinal evaluation of early Alzheimer's disease using brain perfusion...
  @F:input.pdf @N: 405	 @C:  Near-infrared spectroscopy can detect brain activity...

The parameters in outputs with following meaning:
::
  
  @F: prefix output lines with filename.
  @N: prefix output lines with line number within pdf text.
  @C: indicate the context of matches.

  

3. pdftoc.py
------------
Coming soon...

4. dictviewer.py
----------------
Coming soon...
