import json 
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

        # Convert line breaks to Markdown line breaks
        i = i.replace('\n', '  \n')
        
        # Append the string
        text = text + i
        
    return display(Markdown(text))

def js(json_data):
    """
    Prints JSON data as pretty JSON in Notebook Output fields
    """
    text = json.dumps(json_data, indent=4)
    return display(Markdown(f"```json\n{text}\n```"))