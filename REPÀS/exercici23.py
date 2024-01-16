import json

def generar_json():
    libros = []

    for i in range(1, 5):
        libro = {
            "book": {
                "title": f"Libro{i}",
                "cover": f"Cover{i}.jpg",
                "year": 2000 + i,
                "pages": 100 + i * 10
            }
        }
        libros.append(libro)

    json_content = json.dumps(libros, indent=2)
    print(json_content)

    with open("libros.json", "w") as file:
        json.dump(libros, file, indent=2)

generar_json()
