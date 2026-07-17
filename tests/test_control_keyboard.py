import re
from datetime import datetime, timedelta

import pytest

TIMESTAMP = r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}"


class TestPrintLog:
    def test_prepends_timestamp_and_appends_newline(self, ck, capsys):
        ck.print_log("hello")
        out = capsys.readouterr().out
        assert re.fullmatch(rf"{TIMESTAMP} - hello\n", out)

    def test_honours_custom_end(self, ck, capsys):
        ck.print_log("hello", end="")
        out = capsys.readouterr().out
        assert re.fullmatch(rf"{TIMESTAMP} - hello", out)


class TestCalculaTempoExecucao:
    def test_reports_elapsed_time(self, ck, capsys):
        start = datetime.now() - timedelta(seconds=49)
        ck.calculaTempoExecucao(start)
        out = capsys.readouterr().out
        assert "Finalizando execução" in out
        assert "Tempo decorrido ->" in out
        # elapsed of ~49s should render with a 0:00:49 style prefix
        assert re.search(r"Tempo decorrido -> 0:00:49", out)


class TestMain:
    def test_bumble_sends_right_and_esc(self, ck, capsys):
        ck.main(likes=4, likes_por_rodada=2, coldstart=1, app="bumble")
        # 4 likes -> each like sends the like button then "esc"
        assert ck.sent_keys == ["right", "esc"] * 4
        assert "Iniciando Likes no bumble" in capsys.readouterr().out

    def test_tinder_sends_enter_and_esc(self, ck, capsys):
        ck.main(likes=6, likes_por_rodada=3, coldstart=1, app="tinder")
        assert ck.sent_keys == ["enter", "esc"] * 6
        assert "Iniciando Likes no tinder" in capsys.readouterr().out

    def test_unknown_app_sends_nothing(self, ck, capsys):
        with pytest.raises(UnboundLocalError):
            ck.main(likes=4, likes_por_rodada=2, coldstart=1, app="hinge")
        out = capsys.readouterr().out
        assert "App hinge não configurado" in out
        assert ck.sent_keys == []

    def test_number_of_rounds_reported(self, ck, capsys):
        ck.main(likes=50, likes_por_rodada=10, coldstart=1, app="bumble")
        out = capsys.readouterr().out
        assert "Serão feitas 5 rodadas de 10 likes, totalizando 50 likes" in out
        assert "Rodada 5/5" in out
        assert "50 likes executados" in out

    def test_total_key_events_matches_likes(self, ck):
        ck.main(likes=30, likes_por_rodada=10, coldstart=1, app="bumble")
        # each of the 30 likes triggers a like key + an esc key
        assert len(ck.sent_keys) == 60

    def test_coldstart_countdown_sleeps_between_seconds(self, ck, monkeypatch):
        sleep_calls = []
        monkeypatch.setattr(ck, "sleep", lambda seconds: sleep_calls.append(seconds))
        ck.main(likes=2, likes_por_rodada=1, coldstart=4, app="bumble")
        # coldstart loop sleeps once per second in range(1, coldstart) = 3 one-second waits
        assert sleep_calls.count(1) == 3
        # each like waits 0.8s before pressing esc
        assert sleep_calls.count(0.8) == 2
