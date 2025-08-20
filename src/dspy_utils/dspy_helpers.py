import dspy
from common.utils import md

def md_dspy(obj):
    """
    Render a dspy object in markdown format."""
    
    if isinstance(obj, dspy.primitives.prediction.Prediction):
        
        
        """"
        Mappings: 
            obj._store is a dictionary of Fields. 
            obj._store['is_match'] 
        """
        
        # Prediction
        md("**Prediction**: ", obj.prediction)
        
        # ReAct
        md("**Answer**: ", obj.answer)
        md("**Reasoning**: ", obj.reasoning)    
        md("**Trajectory**:")
        for key, value in obj.trajectory.items():
            md("* **", key, "**: ", value)
    
        return

    raise ValueError("Could not match obj to type")
            
