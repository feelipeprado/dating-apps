import keyboard
from time import sleep
from datetime import datetime

from utils import (
    APP_CONFIG,
    calcula_tempo_execucao,
    print_log,
    print_section,
    print_separator,
)


def main(likes, likes_por_rodada, coldstart, app):
    print_section(f"Iniciando Likes no {app}")
    data_hora_inicio = datetime.now()
    rodadas = int(likes / likes_por_rodada)
    print_log(f"Serão feitas {rodadas} rodadas de {likes_por_rodada} likes, totalizando {likes} likes")

    config = APP_CONFIG.get(app)
    if config is None:
        print_log(f"App {app} não configurado...")
        return
    print_log(config["prompt"])
    button = config["button"]

    print_log(f"Inicio em {coldstart} segundos", end='')
    for _ in range(1, coldstart):
        print(".", end='')
        sleep(1)

    print("")
    print_separator()
    print_log("Executando")
    print_separator(end='')

    for cont_rodada in range(1, rodadas + 1):
        print("")
        print_log(f"Rodada {cont_rodada}/{rodadas}", end='\t-\t')
        for cont in range(1, likes_por_rodada + 1):
            print(str(cont)[-1], end='')
            keyboard.send(button)
            sleep(0.8)
            keyboard.send("esc")
    print("")
    calcula_tempo_execucao(data_hora_inicio)
    print_log(f"{likes} likes executados")
    print_separator()


likes = 4500
likes_por_rodada = 10
coldstart = 10 # segundos para iniciar os likes
app = "bumble"  # tinder / bumble
main(likes, likes_por_rodada, coldstart, app)

# 1 min = 75 likes
# 10 min = 750 likes
# 1 h = 4.500 likes
