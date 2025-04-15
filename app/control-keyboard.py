import keyboard
from time import sleep
from datetime import datetime


def print_log(log, end="\n"):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{dt_string} - {log}", end=end)


def calculaTempoExecucao(data_hora_inicio):
    data_hora_fim = datetime.now()
    tempo_exec = data_hora_fim - data_hora_inicio
    print_log(70 * "-")
    print_log("Finalizando execução")
    print_log(f"Tempo decorrido -> {tempo_exec}")


def main(likes, likes_por_rodada, coldstart, app):
    print_log(70 * "-")
    print_log(f"Iniciando Likes no {app}")
    print_log(70 * "-")
    data_hora_inicio = datetime.now()
    rodadas = int(likes / likes_por_rodada)
    print_log(f"Serão feitas {rodadas} rodadas de {likes_por_rodada} likes, totalizando {likes} likes")

    if app == 'tinder':
        print_log("Abra o Tinder, dê o primeiro like manualmente para se preparar...")
        button = 'enter'
    elif app == 'bumble':
        print_log("Abra o Bumble e clique em qualquer lugar da tela para se preparar...")
        button = 'right'
    else:
        print_log(f"App {app} não configurado...")

    print_log(f"Inicio em {coldstart} segundos", end='')
    for seconds in range(1, coldstart):
        print(".", end='')
        sleep(1)

    print("")
    print_log(70 * "-")
    print_log("Executando")
    print_log(70 * "-", end='')

    cont_rodada = 1
    while cont_rodada <= rodadas:
        print("")
        print_log(f"Rodada {cont_rodada}/{rodadas}", end='\t-\t')
        cont = 1
        while cont <= likes_por_rodada:
            print(str(cont)[-1], end='')
            keyboard.send(button)
            sleep(0.8)
            keyboard.send("esc")
            cont += 1
        cont_rodada += 1
    print("")
    calculaTempoExecucao(data_hora_inicio)
    print_log(f"{likes} likes executados")
    print_log(70 * "-")


likes = 4500
likes_por_rodada = 10
coldstart = 10 # segundos para iniciar os likes
app = "bumble"  # tinder / bumble
main(likes, likes_por_rodada, coldstart, app)

# 1 min = 75 likes
# 10 min = 750 likes
# 1 h = 4.500 likes
