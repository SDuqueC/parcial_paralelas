import os
import json
import datetime
import lector_json
import descarga_video
import extraer_audio

import threading





informacion_de_edscargas = []





# Nombre: d_v_y_e_a - Sus siglas significan "Descargar Video Y Extraer Audio" 
# Acciones: 
#   1. Descargar un video de youtube en formato .webm
#   2. Extraer el audio del video descargado en formato .mp3 
#   2. Eliminar el video descargado despues de extraer su audio
#   3. Agregar la informacion de la descarga a un .json llamado registro_de_descargas / Agregar el diccionario con informcion de la descarga y extraccion a una lista
def d_v_y_e_a(numero_de_video, url_y_nombre):

    numero_de_video_str = str(numero_de_video)
    video = url_y_nombre[1] + numero_de_video_str

    fecha_de_subida, url_real = descarga_video.download_video(url_y_nombre[0], video, numero_de_video_str)

    video = video + '.webm'
    audio = url_y_nombre[1] + numero_de_video_str + '.mp3'

    extraer_audio.extract_audio(video, audio)



    os.remove(video)
    print(f"El video {video} ha sido eliminado correctamente.")



    # with open("registro_de_descargas.json", "r") as archivo_json:
    #     datos_de_descargas = json.load(archivo_json)

    # numero_descargas = len(datos_de_descargas)

    descarga_X = {
        "video": video,
        "audio": audio,
        "url": url_real,
        "fecha de subida a youtube": fecha_de_subida,
        "fecha de descarga": datetime.datetime.now().strftime("%Y-%m-%d %H")
    }

    # descarga_x = "descarga " + str(numero_descargas + 1)
    # datos_de_descargas[descarga_x] = descarga_X

    # with open("registro_de_descargas.json", "w") as archivo_json:
    #     json.dump(datos_de_descargas, archivo_json, indent=4)

    global informacion_de_edscargas
    informacion_de_edscargas.append(descarga_X)

    return True





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





threads = []

for url_y_nombre in urls_y_nombres:

    for numero_de_video in range(1, 2): 
        
        thread = threading.Thread(target = d_v_y_e_a, args=(numero_de_video, url_y_nombre))
        
        thread.start()
        
        threads.append(thread)





for thread in threads:
    thread.join()





for informacion_de_edscarga in informacion_de_edscargas:

    with open("registro_de_descargas.json", "r") as archivo_json:
        datos_de_descargas = json.load(archivo_json)

    numero_descargas = len(datos_de_descargas)

    descarga_x = "descarga " + str(numero_descargas + 1)
    datos_de_descargas[descarga_x] = informacion_de_edscarga

    with open("registro_de_descargas.json", "w") as archivo_json:
        json.dump(datos_de_descargas, archivo_json, indent=4)
