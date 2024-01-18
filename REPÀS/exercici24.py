import json

def leer_json():
    with open("libros.json", "r") as file:
        libros = json.load(file)
        json_content = json.dumps(libros, indent=2)
        print(json_content)

# Llamar a la función para leer y mostrar el JSON
leer_json()
