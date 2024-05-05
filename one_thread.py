import os
import json
import datetime
import lector_json
import descarga_video
import extraer_audio





datos_de_descargas_inicial = {
    # "descarga X": {
    #     "video": "video X",
    #     "url": "url X",
    #     "fecha de subida a youtube": "fecha de subida X",
    #     "fecha de descarga": "fecha de descarga X",
    # }
}

nombre_archivo = "registro_de_descargas.json"

with open(nombre_archivo, "w") as archivo_json:
    json.dump(datos_de_descargas_inicial, archivo_json)





urls_y_nombres = lector_json.leer_json('urls_y_nombres.json')





videos_por_canal = 1

for url_y_nombre in urls_y_nombres:

    for numero_de_video in range(1, videos_por_canal + 1):

        numero_de_video_str = str(numero_de_video)
        video = url_y_nombre[1] + numero_de_video_str

        fecha_de_subida, url_real = descarga_video.download_video(url_y_nombre[0], video, numero_de_video_str)

        video = video + '.webm'
        audio = url_y_nombre[1] + numero_de_video_str + '.mp3'

        extraer_audio.extract_audio(video, audio)



        os.remove(video)
        print(f"El video {video} ha sido eliminado correctamente.")



        with open("registro_de_descargas.json", "r") as archivo_json:
            datos_de_descargas = json.load(archivo_json)

        numero_descargas = len(datos_de_descargas)

        descarga_X = {
            "video": video,
            "audio": audio,
            "url": url_real,
            "fecha de subida a youtube": fecha_de_subida,
            "fecha de descarga": datetime.datetime.now().strftime("%Y-%m-%d %H")
        }

        descarga_x = "descarga " + str(numero_descargas + 1)
        datos_de_descargas[descarga_x] = descarga_X

        with open("registro_de_descargas.json", "w") as archivo_json:
            json.dump(datos_de_descargas, archivo_json, indent=4) 
