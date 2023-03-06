import requests

def main():
    
    pokemon = get_specific_pokemon(search_term="pikachu")
    pass

def get_specific_pokemon(search_term):
    #search_term.strip().lower()
    POKE_API_URL = f'https://pokeapi.co/api/v2/pokemon/{search_term}'
    resp_message = requests.get(POKE_API_URL)
    
    if resp_message.ok:
        print(f'Abilities of {search_term} pokemon are:')
        body_contain = resp_message.json()
        for a in body_contain['abilities']:
            print(a['ability']['name'])
        return body_contain
    else:
        return None
    
if __name__ == "__main__":
    main()

