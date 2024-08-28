#scraping the web 'lyngsat' to get the carrier's parameters of open TV broadcasts from Argentina

import urllib.request, json
from lxml.html import fromstring
from parametrizador import parametrizador

#initializing lists

item_list = []
funct_list = []
signal_list = []

#main scraping and list generation process

url = "https://www.lyngsat.com/freetv/Argentina.html"
req = urllib.request.Request(url)
page = urllib.request.urlopen(req)
content = page.read()
document = fromstring(content)
elements = document.find_class("bigtable")          
text = str(elements[0].text_content())
cad = text.split("\n")
for item in cad:
    if (item == '' or item == "LyngSat Stream"):
        #cad.remove(item)
        pass
    else:
        item_list.append(item)
parameters = item_list[41:-35:1]
for parameter in parameters:
    funct_list.append(parameter)
    if (parameter == "HD" or parameter == "SD" or parameter == "A24"):
        if (len(funct_list)) == 8:
            signal_list.append(parametrizador(funct_list))
            funct_list = []
        else:
            funct_list = []
    else:
        pass

#dumpint the dictionary into a json file

signals_json = json.dumps(signal_list)
file = open("scrap/open_arg_tv_signals.json", "w")
file.writelines(signals_json)
file.close()
