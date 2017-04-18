def data_type(var):
  if isinstance(var, str):
    return len(var)
    
  if var == None:
    return 'no value'
  
  if isinstance(var, bool):
    return var

  if isinstance(var, int):
    if var < 100:
      return 'less than 100'
    if var > 100:
      return 'more than 100'
    if var == 100:
      return 'equal than 100'
  
  if isinstance(var, list):
    if len(var) > 2:
      return var[2]
    else:
      return None
  
