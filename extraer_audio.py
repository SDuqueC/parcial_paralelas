import subprocess

def extract_audio(video_entrada, audio_salida):
    """
    Extrae el audio de un video utilizando ffmpeg.
    
    Args:
    - video_entrada (str): La ruta al archivo de video de entrada.
    - audio_salida (str): La ruta al archivo de audio de salida.
    
    Returns:
    - bool: True si la extracción fue exitosa, False en caso contrario.
    """
    try:
        # proceso = None
        # # Ejecutar el comando ffmpeg para extraer el audio
        # try:
        #     proceso = subprocess.run(['ffmpeg', '-i', video_entrada, '-vn', '-acodec', 'copy', audio_salida], capture_output=True, text=True)
        # except FileNotFoundError:
        #     proceso = subprocess.run(['ffmpeg', '-i', video_entrada, '-vn', '-acodec', 'libmp3lame', '-q:a', '2', audio_salida], capture_output=True, text=True)

        proceso = subprocess.run(['ffmpeg', '-i', video_entrada, '-vn', '-acodec', 'libmp3lame', '-q:a', '2', audio_salida], capture_output=True, text=True)

        if proceso.returncode == 0:
            print(f"El audio ha sido extraído correctamente a {audio_salida}.")
            return True
        else:
            print(f"Error al extraer el audio: {proceso.stderr}")
            return False
    except FileNotFoundError:
        print("Error: ffmpeg no está instalado o no se encuentra en el PATH.")
        return False
