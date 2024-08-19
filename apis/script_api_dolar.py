import http.client
import json

def api_consulta(dominio, seccion) -> json:                 #Genera el request a la API
    com = http.client.HTTPSConnection(dominio)                         
    com.request("GET", seccion)
    ans = com.getresponse()
    print(f"\nRespuesta: {ans.status}, {ans.reason}\n")
    data = ans.read()
    return data

def columna(datos) -> str:                                  #Recorre la lista de diccionarios y los muestra en una columna              
    for item in datos:                                             
        for k,v in item.items():
            palabras = str(f"{k}: ") + str(v)
            print(palabras)
        print("\n")

data = api_consulta(dominio="dolarapi.com", seccion="/v1/dolares")
datos = json.loads(data)                                                #Convierto los datos json a una lista con diccionarios
columna(datos)