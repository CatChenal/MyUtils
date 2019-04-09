# -*- coding: utf-8 -*-

def format_with_bold(s_format):
    """
    Returns the string with all placeholders preceded by '_b' 
    replaced with a bold indicator value (ANSI escape code).
    
    :param: s_format: a string format; 
            if contains '_b{}b_' this term gets bolded.
    :param: s: a string or value
    
    :note 1: '... _b{}; something {}b_ ...' is a valid format.
    :note 2: IndexError is raised using the returned format only when
            the input tuple length < number of placeholders ({});
            it is silent when the later are greater (see Example).
    :TODO: Do same for _f{}f_: to frame a text.
    
    :Example:
    # No error:
    fmt = 'What! _b{}b_; yes: _b{}b_; no: {}.'
    print(format_with_bold(fmt).format('Cat', 'dog', 3, '@no000'))
    # IndexError:
    print(format_with_bold(fmt).format('Cat', 'dog'))
    """

    # Check for paired markers:
    if s_format.count('_b') != s_format.count('b_'):
        err_msg1 = "Bold indicators not paired. Expected '_b{}b_'."
        raise LookupError(err_msg1)
    
    # Check for start bold marker:
    b1 = '_b'
    i = s_format.find(b1 + '{')
    
    # Check marker order: '_b' past 'b_'?:
    if i > s_format.find('}' + 'b_'):
        err_msg2 = "Starting bold indicator not found. Expected '_b{}b_'."
        raise LookupError(err_msg2)
        
    while i != -1:
        
        # Check for trailing bold marker:
        b2 = 'b_'
        j = s_format.find('}' + b2)
        
        if j != -1:
            s_format = s_format.replace(b1, '\033[1m')
            s_format = s_format.replace(b2, '\033[0m')
        else:
            err_msg3 = "Trailing bold indicator not found. Expected '_b{}b_'."
            raise LookupError(err_msg3)
            
        i = s_format.find(b1 + '{')
    
    return s_format


def test_format_with_bold(s_format):
    # remove trailing marker(s):
    s_format = s_format.replace('b_','')
    return format_with_bold(s_format)
