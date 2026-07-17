from datetime import datetime

SEPARATOR = 70 * "-"

APP_CONFIG = {
    "tinder": {
        "button": "enter",
        "prompt": "Abra o Tinder, dê o primeiro like manualmente para se preparar...",
    },
    "bumble": {
        "button": "right",
        "prompt": "Abra o Bumble e clique em qualquer lugar da tela para se preparar...",
    },
}


def print_log(log, end="\n"):
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{dt_string} - {log}", end=end)


def print_separator(end="\n"):
    print_log(SEPARATOR, end=end)


def print_section(title):
    print_separator()
    print_log(title)
    print_separator()


def calcula_tempo_execucao(data_hora_inicio):
    tempo_exec = datetime.now() - data_hora_inicio
    print_separator()
    print_log("Finalizando execução")
    print_log(f"Tempo decorrido -> {tempo_exec}")
