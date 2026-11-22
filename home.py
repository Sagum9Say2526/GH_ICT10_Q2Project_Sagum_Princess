from pyscript import document
#all the nicknames of the countries
nicknames = {
    "brunei": "The Abode of Peace",
    "cambodia": "The Kingdom of Wonder",
    "indonesia": "The Emerald of the Equator",
    "laos": "The Land of a Million Elephants",
    "malaysia": "The Golden Peninsula",
    "myanmar": "The Golden Land",
    "philippines": "The Pearl of the Orient Seas",
    "singapore": "The Lion City",
    "thailand": "The Land of Smiles",
    "timor-leste": "The Land of the Rising Sun",
    "vietnam": "The Land of the Blue Dragon"
}


def nickname(event=None):
    #this gets what the ehh user typed, removes the extra spaces and automatically makes all of it lowercase
    country = document.getElementById("country").value.lower().strip()
    #checks the nicknames to see if the country is in there and if it isnt it displays "Country not identified."
    document.getElementById("result").innerText = nicknames.get(country, "Country not identified.")