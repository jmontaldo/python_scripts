#You can use this mod if you want to save the json locally in your machine to check.

"""
from scrap import scrapper
from pathlib import Path
import json

#setting the file's path

directory = str(Path(__file__).parent.resolve())
path = directory + "/open_col_tv_signals.json"

#dumping the dictionary into a json file

signal_list = scrapper("Colombia")
response = json.dumps(signal_list)
file = open(path, "w")
file.writelines(response)
file.close()                        
"""