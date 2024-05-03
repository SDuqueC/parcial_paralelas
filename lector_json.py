import json

def leer_urls_desde_json(archivo):
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
            urls = [video["url"] for video in data["videos"]]
        return urls
    except FileNotFoundError:
        print("Error: El archivo JSON no se encontró.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo JSON no es válido.")
        return []
