from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_data = None
    error = None

    if request.method == "POST":
        name = request.form["pokemon"].lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            pokemon_data = {
                "name": data["name"].capitalize(),
                "experience": data["base_experience"],
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "image": data["sprites"]["front_default"]
            }
        else:
            error = f"No se encontró el Pokémon '{name}'."

    return render_template("index.html", pokemon=pokemon_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)