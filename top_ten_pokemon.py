# import packages
import urllib.request as urlreq
import json
from pprint import pprint
import pickle
from time import sleep
import sys
import os


# set the url variable
urlPokemon = r'https://pokeapi.co/api/v2/pokemon/?limit=949&offset=0'

# function to load the JSON file
def json_req(url_to_request):
    req = urlreq.Request(

        url_to_request,
        data=None,
        headers={
            'User-Agent': 'just some guy 0.1'
        }
    )
    return json.loads(urlreq.urlopen(req).read().decode())

# save the JSON data to the hard drive using pickle
urlPokemon = r'https://pokeapi.co/api/v2/pokemon/?limit=949&offset=0'
pokemon_json_data = json_req(urlPokemon)
pickle.dump(json_req(urlPokemon), open("C:\data\pokemon\pokemon.p", "wb"))

# open the pickle file for consumption
pokemon_pkl_data = pickle.load( open( "C:\data\pokemon\pokemon.p", "rb" ) )
pokemon_name_and_url_list = pokemon_pkl_data['results']

# getting pokemon data - loop through the pokemon_name_and_url_list, req the data and store in pickle
 for i in pokemon_name_and_url_list:
	while True:
		try:
            ll = pickle.dump(json_req(i['url']), open("C:\data\pokemon\pokemon_scores\{name}.p".format(name=i['name']), "wb"))
            pprint(ll)
        except:
            print(sys.exc_info()[1])
            sleep(3)
            continue
		break

# # create dictionary where all pokemon will be stored
pokemon_dict = {}
#
# loop through all pokemon files and insert into dictionary
 for file in os.listdir("C:\data\pokemon\pokemon_scores"):
    if file.endswith(".p"):
        pokemon_file = pickle.load( open( "C:\data\pokemon\pokemon_scores\{f}".format(f=file), "rb" ) )
        pokemon_dict[pokemon_file['name']] = pokemon_file['stats'][4]['base_stat']

# make pickle file from the pokemon_dict so it is always accessible without the for loop
 pickle.dump(pokemon_dict, open("C:\data\pokemon\pokemon_scores\pokemon_attack_scores.p", "wb"))

# assign the prev pickle dump to a variable in memory so we can manipulate
pokemon_attack_scores = pickle.load( open( "C:\data\pokemon\pokemon_scores\pokemon_attack_scores.p", "rb" ) )

pprint(sorted(pokemon_attack_scores.items(), key=lambda x : x[1], reverse = False))

# top 10 pokemon with attack score
# ('gallade-mega', 165),
# ('rampardos', 165),
# ('garchomp-mega', 170),
# ('kyurem-black', 170),
# ('deoxys-attack', 180),
# ('groudon-primal', 180),
# ('rayquaza-mega', 180),
# ('kartana', 181),
# ('heracross-mega', 185),
# ('mewtwo-mega-x', 190)]