'''
@summary: Normalizer, text normalizing.

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: normalizer.py 2012-03-28 Micle Bu
'''
import re
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')

def normalize_whitespace(s):
    """ 
    Returns a string that has at most one whitespace
    character between non-whitespace characters. 

    >>> normalise_whitespace(' hi   there')
    ' hi there'
    >>> normalise_whitespace('meh\n\n\f')
    'meh '
    """
    s = re.sub(r'\s+', ' ', s)
    s = s.strip()
    return re.sub(r'\s+', ' ', s) 

def normalize_linkbreak(s):
    pattern = re.compile(r'\n\s*[A-Z]')
    mc = pattern.search(s)
    while mc:
        replace = re.sub(r'\s+', '<!-- start line break -->', mc.group())
        s = re.sub(r'\n\s*[A-Z]', replace, s, 1)
        mc = pattern.search(s)
    return s

def normalize_hyphen(s):
    return re.sub(r'-\s', '', s)

def normalize_references(s):
    s = re.sub('References', 'References\n', s)
    return s

def normalize_break(s):
    """
    Normalise paragraph-break, link-break, hyphen and whitespace:
    1.extra line-break and whitespace will be removed 
    2.paragraph-break, we choose r'\n\n', will be preserved
    3.link-break, we choose r'\.\s*\n' and r'\n\s*[A-Z]', will be preserved
    4.hyphen, we choose r'-\s', will be removed
    
    """
    # normalize
    s = re.sub(r'\n{2}', '<!-- paragraph break -->', s)
    s = re.sub(r'\.\s*\n', '<!-- end line break -->', s)
    s = normalize_linkbreak(s)
    s = normalize_whitespace(s)
    # preserve
    s = re.sub(r'<!-- start line break -->', '\n', s)
    s = re.sub(r'<!-- end line break -->', '.\n', s)
    s = re.sub(r'<!-- paragraph break -->', '\n\n', s)
    # dehyphen
    s = normalize_hyphen(s)
    s = normalize_references(s)
    return s

def normalize_pattern(s):
    s = re.sub('\s+', '<-- space -->', s)
    s = re.sub('<-- space -->', '\s*', s)
    return s

def normalize_special_character(s):
    return re.sub(r"""[\\/:"*?<>|().']+""", '',s)

def normalize_title(s):
    """
    Normalise whitespace and casesensitive:
    1.extra line-break and whitespace will be removed
    2.strip the string 
    3.lower case
    """
    s = s.decode('ascii','ignore').encode('utf-8', 'ignore')
    s = normalize_whitespace(s)
    return s.lower()

def normalize_toc_item(s):
    """
    Normalise whitespace and casesensitive:
    1.extra line-break and whitespace will be removed
    2.strip the string 
    3.lower case
    """
    s = s.decode('ascii','ignore').encode('utf-8', 'ignore')
    s = normalize_whitespace(s)
    s = s.strip()
    s = normalize_special_character(s)
    return s.lower()