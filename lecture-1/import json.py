import json

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
identificacion = input("Ingrese su identificación: ")

# Almacenar en un diccionario
usuario = {
    "nombre": nombre,
    "identificacion": identificacion
}

# Guardar el diccionario en un archivo JSON
with open("usuario.json", "w", encoding="utf-8") as archivo:
    json.dump(usuario, archivo, ensure_ascii=False, indent=4)

print("Datos guardados en usuario.json")