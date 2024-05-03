import os
import lector_json
import descarga_video
import extraer_audio

# nombre_v_a = "Faded Into You"

urls_y_nombres = lector_json.leer_json('urls_y_nombres.json')

for url_y_nombre in urls_y_nombres:

    for numero_de_video in range(1, 6):

        numero_de_video_str = str(numero_de_video)
        video = url_y_nombre[1] + numero_de_video_str

        descarga_video.download_video(url_y_nombre[0], video, numero_de_video_str)

        video = video + '.webm'
        audio = url_y_nombre[1] + numero_de_video_str + '.mp3'

        extraer_audio.extract_audio(video, audio)

        archivo = video

        os.remove(archivo)
        print(f"El video {video} ha sido eliminado correctamente.")
