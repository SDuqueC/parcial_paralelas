import os
import json
import datetime
import lector_json
import descarga_video
import extraer_audio
import multiprocessing
import time


# Función para calcular el tiempo de ejecución
def calcular_tiempo_ejecucion(tiempo_inicio):
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

# Nombre: d_v_y_e_a - Sus siglas significan "Descargar Video Y Extraer Audio"
# Acciones:
#   1. Descargar un video de youtube en formato .webm
#   2. Extraer el audio del video descargado en formato .mp3
#   2. Eliminar el video descargado despues de extraer su audio
#   3. Agregar la informacion de la descarga a un .json llamado registro_de_descargas / Agregar el diccionario con informcion de la descarga y extraccion a una lista
def d_v_y_e_a(numero_de_video, url_y_nombre):
    numero_de_video_str = str(numero_de_video)
    video = url_y_nombre[1] + numero_de_video_str

    # Inicio de la medición de tiempo de ejecución de la descarga y extracción de audio
    tiempo_inicio_descarga = time.time()

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

    global informacion_de_descargas
    global cero_a_numero_de_videos_menos_uno
    informacion_de_descargas[cero_a_numero_de_videos_menos_uno] = descarga_X
    cero_a_numero_de_videos_menos_uno += 1

    # Fin de la medición de tiempo de ejecución de la descarga y extracción de audio
    tiempo_total_descarga = calcular_tiempo_ejecucion(tiempo_inicio_descarga)
    print(f"Tiempo de descarga y extracción para el video {video}: {tiempo_total_descarga} segundos")

    return True



def main(procesos):
    maximo_de_procesos_activos = procesos

    videos_por_canal = 5

    informacion_de_descargas = []

    # Inicio de la medición de tiempo total de ejecución
    tiempo_inicio_total = time.time()

    with open("urls_y_nombres.json", "r") as archivo_json:
        canales = json.load(archivo_json)

    numero_de_videos = len(canales['canales']) * videos_por_canal

    for xd in range(0, numero_de_videos):
        informacion_de_descargas.append(0)

    cero_a_numero_de_videos_menos_uno = 0



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

    processes = []

    for url_y_nombre in urls_y_nombres:

        for numero_de_video in range(1, videos_por_canal + 1):

            # numero_de_procesos_activos = len(multiprocessing.active_children())
            # print("Procesos en ejecucion:", numero_de_procesos_activos)
            # while (numero_de_procesos_activos >= maximo_de_procesos_activos):
            #     numero_de_procesos_activos = len(multiprocessing.active_children())

            process = multiprocessing.Process(target=d_v_y_e_a, args=(numero_de_video, url_y_nombre))

            process.start()

            processes.append(process)

    for process in processes:
        process.join()

    for informacion_de_descarga in informacion_de_descargas:
        with open("registro_de_descargas.json", "r") as archivo_json:
            datos_de_descargas = json.load(archivo_json)

        numero_descargas = len(datos_de_descargas)

        descarga_x = "descarga " + str(numero_descargas + 1)
        datos_de_descargas[descarga_x] = informacion_de_descarga

        with open("registro_de_descargas.json", "w") as archivo_json:
            json.dump(datos_de_descargas, archivo_json, indent=4)

    # Fin de la medición de tiempo total de ejecución
    tiempo_total_total = calcular_tiempo_ejecucion(tiempo_inicio_total)
    print(f"Tiempo total de ejecución: {tiempo_total_total} segundos")
    return tiempo_total_total
