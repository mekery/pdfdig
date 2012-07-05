PDFDig Release
==================================================

PDFDig 0.2 (released 2012-04-19)
--------------------------------------------------
This is a update release. 

**New Features**

- Match: Support sentence-based context of matches.
- Match: Support highlight the matches.
- pdfgrep: Support search all files under each directory. 
- pdfgrep: Add highlight option.

**Fixes**

- Text: Fix cross-platform check for pdftotext

PDFDig 0.1 (released 2012-04-10)
--------------------------------------------------
This is the initial release. 

**New Features**

- Text: Convert PDF to text using 'pdftotext' and normalize the text. Store text lines as an list object.
- Match: Pattern matching based on Text. Store matches as an list object.
- TOC: Build the Table of Content(TOC) of PDF document, filtering by a provided TOC dictionary.
- pdftotext: a (Command Line Interface) CLI utility based on Text.
- pdfgrep: a CLI utility based on Match.
- pdftoc: a CLI utility based on TOC

Refer to :doc:`intro` to see the details of New Features.