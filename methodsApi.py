import requests
import json
"""Get -->pedir recursos del servidor"""
def content(): #imprime html
    url= 'http://httpbin.org/get'
    response= requests.get(url)
    #print (response)
    if response.status_code == 200:
        print (response.content) 
        """
        file=open('google.html','wb')
        file.write(response.content)
        file.close()
        """
def meetGet(): 
    url= 'http://httpbin.org/get'
    args={'nombre' :'daniel','curso':'python'}
    response=requests.get(url, params=args)
    if response.status_code==200:
        #return string
        #print(response.content)
        #return dictionary
        #print (response.json())
        #return 'origin' of the dictionary
        print(response.json()['origin'])
def usarLibJson():
    url= 'http://httpbin.org/get'
    args={'nombre':'daniel','category':'persona'}
    response= requests.get(url,params=args)
    if response.status_code==200:
        responseJson=json.loads(response.text)
        origin=responseJson['origin']
        print(origin)
"""POST --> crear recursos dentro del servidor"""
def meetPost():
    url='http://httpbin.org/post'
    payload={'nombre':'daniel','hola':'chao'}
    response=requests.post(url,json=payload) #serializar->pasar el dict a un obj json
    #se envian los datos dentro del atributo data y se crea un nuevo dict con nombre json -> json se encarga de serializarlos
    #tambien se puede usar data=payload y los atributos van a forms -> debemos serealizarlos nosotros con data=json.dumps(payload)
    if response.status_code==200:
        print (response.json())
def encabezado():
    url='http://httpbin.org/post'
    payload={'nombre':'daniel','hola':'chao'}
    headers={ 'Content-Type' : 'application/json', 'access-token':'12345' }
    response=requests.post(url,data=json.dumps(payload),headers=headers)
    if response.status_code==200:
        headers_response=response.headers
        print (headers_response)
"""PUT --> actualizar"""
def meetPut():
    url='http://httpbin.org/put'
    payload={'nombre':'daniel','hola':'chao'}
    headers={ 'Content-Type' : 'application/json', 'access-token':'18345' }
    response=requests.put(url,data=json.dumps(payload),headers=headers)
    if response.status_code==200:
        print (response.headers)
"""DELETE --> borrar contenido"""
def meetDelete():
    url='http://httpbin.org/delete'
    payload={'nombre':'daniel','hola':'chao'}
    headers={ 'Content-Type' : 'application/json', 'access-token':'18345' }
    response=requests.delete(url,data=json.dumps(payload),headers=headers)
    if response.status_code==200:
        print (response.headers)
"""CHUNKS --> conseguir archivos pesados"""
def meetChunks():
    url='https://www.hola.com/imagenes/estar-bien/20190820147813/razas-perros-pequenos-parecen-grandes/0-711-550/razas-perro-pequenos-grandes-m.jpg'
    response=requests.get(url,stream=True) #Stream permite dejar la conexion abierta mientras se descarga el contenido
    with open('image.jpg','wb') as file: #with -> manejo de excepciones para archivos (with <-> try:/finally:)
        for chunk in response.iter_content(): #lee de a poco los contenidos solicitados
            file.write(chunk)#va escribiendo los datos obtenidos
    response.close()#cerrar la conexion

"""
pass 
In Python, pass is a null statement.
The interpreter does not ignore a pass statement, but nothing happens and the statement results into no operation.
The pass statement is useful when you don’t write the implementation of a function but you want to implement it in the future.
"""
"""
Endpoint => URL
"""