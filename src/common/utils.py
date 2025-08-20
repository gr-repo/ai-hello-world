 
from IPython.display import Markdown, display
  
def md(*args):
    """
    Prints values as Markdown in Notebook Output fields
    """
    text = ''
    for i in args:
        i = str(i)
        
        # Add a line break if empty string
        if len(i) == 0:
            text = text + '\n\n'
            continue
        
        # Append the string
        text = text + i
        
    return display(Markdown(text))