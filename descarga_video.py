import os
import subprocess

def download_video(url, nombre_archivo_salida):
    """
    Descarga un video desde una URL utilizando yt-dlp.
    
    Args:
    - url (str): La URL del video a descargar.
    - nombre_archivo_salida (str): El nombre del archivo de salida para el video descargado, 
                                   que puede incluir una ruta completa.
    
    Returns:
    - bool: True si la descarga fue exitosa, False en caso contrario.
    """
    try:
        # Crear el directorio si no existe
        directorio = os.path.dirname(nombre_archivo_salida)
        if directorio:
            os.makedirs(directorio, exist_ok=True)

        # Ejecutar el comando yt-dlp para descargar el video
        proceso = subprocess.run(['yt-dlp', '-o', nombre_archivo_salida, url], capture_output=True, text=True)
        if proceso.returncode == 0:
            print(f"El video {nombre_archivo_salida} ha sido descargado correctamente.")
            return True
        else:
            print(f"Error al descargar el video {nombre_archivo_salida}: {proceso.stderr}")
            return False
    except FileNotFoundError:
        print("Error: yt-dlp no está instalado o no se encuentra en el PATH.")
        return False
