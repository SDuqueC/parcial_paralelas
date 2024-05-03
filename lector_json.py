import json

def leer_json(archivo):
    """
    Lee las URLs de video desde un archivo JSON y las devuelve como una lista.
    
    Args:
    - archivo (str): La ruta al archivo JSON.
    
    Returns:
    - list: Una lista de URLs de video.
    """
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            urls_y_nombres = [(video["url"], video["nombre"]) for video in data["videos"]]
        return urls_y_nombres
    except FileNotFoundError:
        print("Error: El archivo JSON no se encontró.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo JSON no es válido.")
        return []
