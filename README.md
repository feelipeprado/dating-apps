# Dating Apps

O arquivo `control-keyboard.py` tem como objetivo automatizar os likes nos apps `Bumble` e `Tinder`.

No `Bumble` ele irá pressionar a tecla `seta para direita`, portanto basta executar o `control-keyboard.py`, alternar para o navegador com o `Bumble` aberto e aguardar o início da execução.

No `Tinder` ele irá pressionar a tecla `enter`, portanto basta executar o `control-keyboard.py`, alternar para o navegador com o `Tinder` aberto, dar o like manualmente e aguardar o início da execução.

>Importante mencionar que o `control-keyboard.py` sempre pressiona a tecla `esc` para que os likes não parem em caso de MATCH.

## Parâmetros

Para configurar a execução, ajuste as variáveis abaixo, presentes no final do `control-keyboard.py`:

1. **likes**
   - quantidade total de likes desejado
2. **likes_por_rodada**
   -  quantidade total de likes por rodada, utilize para visualizar melhor a evolução da execução pelos logs
   - caso escolha, por exemplo, 50 like e 10 likes por rodada, o `control-keyboard.py` executará 5 rodadas de 10 likes cada
3. **coldstart**
   - configura o tempo em segundos para inicio da execução, necessário para que o usuário alterne até o navegador
4. **app**
   - escolha `tinder` ou `bumble`

Exemplo de preenchimento:
```python
likes = 4500
likes_por_rodada = 10
coldstart = 10 # segundos para iniciar os likes
app = "bumble"  # tinder / bumble
```

## Métricas

O `control-keyboard.py` foi configurado com `sleep(0.8)`, foi o melhor valor encontrado, menos que isso não otimizava a velocidade pois não dava tempo do site interpretar.

Com isso, alcançamos as seguintes métricas:

- 1 min = 75 likes
- 10 min = 750 likes
- 1 h = 4.500 likes

# Exemplo de Logging

```txt
15/04/2025 19:32:52 - ----------------------------------------------------------------------
15/04/2025 19:32:52 - Iniciando Likes no bumble
15/04/2025 19:32:52 - ----------------------------------------------------------------------
15/04/2025 19:32:52 - Serão feitas 5 rodadas de 10 likes, totalizando 50 likes
15/04/2025 19:32:52 - Abra o Bumble e clique em qualquer lugar da tela para se preparar...
15/04/2025 19:32:52 - Inicio em 10 segundos.........
15/04/2025 19:33:01 - ----------------------------------------------------------------------
15/04/2025 19:33:01 - Executando
15/04/2025 19:33:01 - ----------------------------------------------------------------------
15/04/2025 19:33:01 - Rodada 1/5	-	1234567890
15/04/2025 19:33:09 - Rodada 2/5	-	1234567890
15/04/2025 19:33:17 - Rodada 3/5	-	1234567890
15/04/2025 19:33:26 - Rodada 4/5	-	1234567890
15/04/2025 19:33:34 - Rodada 5/5	-	1234567890
15/04/2025 19:33:42 - ----------------------------------------------------------------------
15/04/2025 19:33:42 - Finalizando execução
15/04/2025 19:33:42 - Tempo decorrido -> 0:00:49.446795
15/04/2025 19:33:42 - 50 likes executados
15/04/2025 19:33:42 - ----------------------------------------------------------------------
```
