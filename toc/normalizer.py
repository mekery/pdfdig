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
    return re.sub(r'\s+', ' ', s) 

def normalize_special_character(s):
    return re.sub(r"""[\\/:"*?<>|().']+""", '',s)

def normalize(s):
    """
    Normalise whitespace and casesensitive:
    1.extra line-break and whitespace will be removed
    2.strip the string 
    3.lower case
    """
    s = s.decode('ascii','ignore').encode('utf-8', 'ignore')
    s = normalize_whitespace(s)
    s = normalize_special_character(s)
    s = s.strip()
    return s.lower()
