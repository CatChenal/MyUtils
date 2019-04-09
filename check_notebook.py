# -*- coding: utf-8 -*-

def check_book():
    """
    Utils to check a Jupyter notebook environment:
    a markdown cell in a jupyter lab notebook cannot render
    variables: the cell text needs to be created with
    IPython.display.Markdown.
    """
    def is_lab_notebook():
        import re
        import psutil
        
        return any(re.search('jupyter-lab-script', x)
                   for x in psutil.Process().parent().cmdline())

    if is_lab_notebook():
        # need to use Markdown if referencing variables:
        from IPython.display import Markdown
        msg = "This is a JupyterLab notebook: Use \
               `IPython.display.Markdown()` if referencing variables."
        return Markdown('### {}'.format(msg))