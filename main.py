import one_thread
import multi_thread
import multi_processing

def main():
    # tiempos = []
    # promedios = []
    #
    # for i in range(4):
    #     tiempo = one_thread.main()
    #     tiempos.append(tiempo)
    #
    # # Hallar el promedio de los tiempos en tiempos
    # promedio = sum(tiempos) / 4
    # promedios.append(promedio)
    #
    # # Se limpia la lista de tiempos
    # tiempos.clear()
    #
    # for i in range(2, 5):
    #     for j in range(4):
    #         tiempo = multi_thread.main(pow(2, i))
    #         tiempos.append(tiempo)
    #     promedio = sum(tiempos) / 4
    #     promedios.append(promedio)
    #     tiempos.clear()
    #
    # for i in range(2, 5):
    #     for j in range(4):
    #         tiempo = multi_processing.main(pow(2, i))
    #         tiempos.append(tiempo)
    #     promedio = sum(tiempos) / 4
    #     promedios.append(promedio)
    #     tiempos.clear()
    #
    # print("Promedios de tiempo de ejecución:\n")
    # print(promedios)
    # tiempo=multi_processing.main(8)
    # print(tiempo)
    tiempo = multi_thread.main(8)
    print(tiempo)

if __name__ == "__main__":
    main()