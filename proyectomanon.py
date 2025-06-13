import requests

def obtener_datos():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if respuesta.status_code == 200:
        print("Datos obtenidos:")
        print(respuesta.json())
    else:
        print("Error al obtener los datos")

if __name__ == "__main__":
    obtener_datos()
