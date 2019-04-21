# -*- coding: utf-8 -*-

def save_file(fname, ext, s, replace=True):
    """
    Usual write method of file handle used with
    json output if stream s is a dict.
    :param: fname: a file name
    :param: ext: output file extension
    :param: replace default (True):: overwrite
    """
    import os

   # check if fname has an extension:
    try:
        i = fname.index('.' , -6)
        outfile = fname[:i] + '.' + ext
    except:
        outfile = fname + '.' + ext
    
    if replace:
        if os.path.exists(outfile):
            os.remove(outfile)

    if isinstance(s, dict):
        import json

        with open(outfile, 'w') as f:
            f.write(json.dumps(s))
    else:
        if len(s):
            with open(outfile, 'w') as f:
                f.write(s)
    return
