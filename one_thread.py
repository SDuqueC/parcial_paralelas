import os
import lector_json
import descarga_video
import extraer_audio

# nombre_v_a = "Faded Into You"

urls_y_nombres = lector_json.leer_json('urls_y_nombres.json')

# video = '.webm'
# audio = '.mp3'

for url_y_nombre in urls_y_nombres:
    video = url_y_nombre[1] + '.webm'
    audio = url_y_nombre[1] + '.mp3'

    descarga_video.download_video(url_y_nombre[0], url_y_nombre[1])

    extraer_audio.extract_audio(video, audio)

    archivo = video

    os.remove(archivo)
    print(f"El video {video} ha sido eliminado correctamente.")
    
