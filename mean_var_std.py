import numpy as np

calculations: dict = dict()

def calculate(valuelist: list)->dict:
    """Calculate various statistical measures for a given list of nine numbers.
    
    Parameters:
        valuelist (list): A list containing exactly nine numerical values.
        
    Returns:
        dict: A dictionary containing the mean, variance, standard deviation, 
         maximum, minimum, and sum of the values in the list. Each key in 
            the dictionary maps to a list of three elements:
            - The first element is the calculation along the columns.
            - The second element is the calculation along the rows.
            - The third element is the overall calculation for the entire list.
    Raises:
        ValueError: If the input list does not contain exactly nine numbers.
    """
    
    if len(valuelist) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array([valuelist[0:3],valuelist[3:6],valuelist[6:9]])
    
    calculations["mean"]               = [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(),matrix.mean()]
    calculations["variance"]           = [matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(),matrix.var()]
    calculations["standard deviation"] = [matrix.std(axis=0).tolist(),matrix.std(axis=1).tolist(),matrix.std()]
    calculations["max"]                = [matrix.max(axis=0).tolist(),matrix.max(axis=1).tolist(),matrix.max()]
    calculations["min"]                = [matrix.min(axis=0).tolist(),matrix.min(axis=1).tolist(),matrix.min()]
    calculations["sum"]                = [matrix.sum(axis=0).tolist(),matrix.sum(axis=1).tolist(),matrix.sum()]
    
    return calculations