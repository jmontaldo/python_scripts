#this function create a dictionary with the parameters given by the generated lists from below

def parametrizador(param_list: list) -> dict:   
    signals = {"signal": param_list[0],         
               "position": param_list[1],
               "satellite": param_list[2],
               "region": param_list[3],
               "eirp": param_list[4],
               "frequency": param_list[5],
               "modulation": param_list[6],
               "feed": param_list[7]}
    return signals