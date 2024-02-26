from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)

#minimum aplication
@app.route("/")
def get_list_character_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", character_list = dict["results"])

#ROTAS PARA OS PERSONAGENS

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters_data = response.read()
    dict = json.loads(characters_data)

    character_list = []

    for character in dict["results"]:
        characters_info = {
            "name": character["name"],
            "status": character["status"],
            "image": character["image"],
            "species": character["species"],
            "gender": character["gender"],
            "origin_name": character["origin"]["name"],
            "location_name": character["location"]["name"]
        }

        character_list.append(characters_info)
    
    return {"characters": character_list}

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    location_url = dict["location"]["url"]
    location_response = urllib.request.urlopen(location_url)
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    dict["location_info"] = location_dict

    return render_template("profile.html", profile = dict)


#ROTAS PARA OS EPISÓDIOS

@app.route("/lista/episodios")
def get_episodios_lista():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes_data = response.read()
    dict = json.loads(episodes_data)

    episodes_list = []

    for episode in dict["results"]:
        episodes_info = {
            "id": episode["id"],
            "name": episode["name"],
            "air_date": episode ["air_date"],
            "episode": episode["episode"],
            "characters": episode["characters"]
        }

        episodes_list.append(episodes_info)
    
    return {"episodes": episodes_list}


def get_character_info(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    character_data = json.loads(data)
    return character_data

@app.route("/episodios")
def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes_list=dict["results"])

@app.route("/episodios/<id>")
def get_episode_details(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episode_data = json.loads(data)

    return render_template("profileEpisodios.html", episode=episode_data, get_character_info=get_character_info)

# ROTAS PARA A LOCALIZAÇÃO

@app.route("/lista/localizacao")
def get_list_location():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    location_data = response.read()
    dict = json.loads(location_data)

    location_list = []

    for local in dict["results"]:
        location_info = {
            "id": local["id"],
            "name": local["name"],
            "type": local["type"],
            "dimension": local["dimension"],
            "residents": local["residents"]
        }

        location_list.append(location_info)
    
    return {"localization": location_list}

def get_resident_info(resident_id):
    url = f"https://rickandmortyapi.com/api/character/{resident_id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    resident_data = json.loads(data)
    return resident_data


@app.route("/location")
def get_list_location_page():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", location_list=dict["results"])

@app.route("/location/<id>")
def get_location_details(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    local_data = json.loads(data)

    return render_template("locationsProfile.html", local=local_data, get_resident_info=get_resident_info)

