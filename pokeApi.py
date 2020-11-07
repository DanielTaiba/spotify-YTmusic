import requests

def getPokemon(offset=0):
    url='https://pokeapi.co/api/v2/pokemon'
    args={'offset': offset} if offset else {}

    response=requests.get(url,params=args)
    #estraer de a 20 pokemon
    if response.status_code==200:
        payload=response.json()
        results=payload.get('results',[])
        if results:
            for pokemon in results:
                print (pokemon['name'])
        next=input('continuar listando? [Y/N]').lower() #next(iterable,default)
        if next=='y':
            getPokemon(offset=offset+20)
    """ #extraer todos los pokemon
    if response.status_code==200:
        payload=response.json()
        while offset<=payload['count']:
            results=payload.get('results',[])
            for pokemon in results:
                print (pokemon['name'])
            getPokemon(offset=offset+20)
    """