# Dating Apps

---
O arquivo `control-keyboard.py` tem como objetivo automatizar os likes nos apps Bumble e Tinder.

No **Bumble** ele irá pressionar a tecla `seta para direita`, portanto basta executar o `control-keyboard.py`, alternar para o navegador com o **Bumble** aberto e aguardar o início da execução.

No **Tinder** ele irá pressionar a tecla `enter`, portanto basta executar o `control-keyboard.py`, alternar para o navegador com o **Tinder** aberto, dar o like manualmente e aguardar o início da execução.

>Importante mencionar que o `control-keyboard.py` sempre pressiona a tecla `esc` para que os likes não parem em caso de MATCH.

## Parâmetros

---
Para configurar a execução, basta ajustar as variáveis abaixo, presentes no final do `control-keyboard.py`:

1. **likes**
   - quantidade total de likes desejada
2. **likes_por_rodada**
   -  quantidade total de like por rodada
   - utilize para visualizar melhor a evolução da execução pelos logs
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

---
O `control-keyboard.py` foi configurado com `sleep(0.8)`, foi o melhor valor encontrado, menos que isso não otimizava a velocidade pois não dava tempo do site interpretar.

Com isso, alcancamos as seguintes métricas:

- 1 min = 75 likes
- 10 min = 750 likes
- 1 h = 4.500 likes

# Exemplo de Logging

---
```txt
15/04/2025 19:28:18 - ----------------------------------------------------------------------
15/04/2025 19:28:18 - Iniciando Likes no bumble
15/04/2025 19:28:18 - ----------------------------------------------------------------------
15/04/2025 19:28:18 - Serão feitas 450 rodadas de 10 likes, totalizando 4500 likes
15/04/2025 19:28:18 - Abra o Bumble e clique em qualquer lugar da tela para se preparar...
15/04/2025 19:28:18 - Inicio em 10 segundos.........
15/04/2025 19:28:27 - ----------------------------------------------------------------------
15/04/2025 19:28:27 - Executando
15/04/2025 19:28:27 - ----------------------------------------------------------------------
15/04/2025 19:28:27 - Rodada 1/450	-	1234567890
15/04/2025 19:28:35 - Rodada 2/450	-	1234567890
15/04/2025 19:28:43 - Rodada 3/450	-	123456
```
