""""
Uma escola está testando um sistema simples de monitoramento ambiental para identificar salas com possível risco de calor excessivo.

Você recebeu uma matriz em que cada linha representa uma sala e cada coluna representa a temperatura registrada em um horário diferente do dia.

sala 1 ------ 24º-----23º
temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

 1. Percorra toda a matriz de temperaturas.
    For encadeado para percorrer linhas e colunas

 2. Calcule a média de temperatura de cada sala (durante o dia).
    Somar os elementos da mesma linha em colunas diferentes.

 3. Identifique quantas vezes cada sala registrou temperatura maior ou igual a 33.
    Condicional temperatura >= 33 com contador para cada linha com elemenos de coluna diferente

 4. Mostre, para cada sala:
    número da sala;
    média das temperaturas;
    quantidade de registros críticos.

    Matriz
    nº  media temp  qtd registro
    1       20          4
    2
    3
    4
 Ao final, informe qual sala teve a maior quantidade de registros críticos.
"""

temp_salas = [
    [28, 31, 34, 33],  # Sala 1
    [25, 27, 29, 28],  # Sala 2
    [32, 35, 36, 34],  # Sala 3
    [24, 26, 25, 27],  # Sala 4
]

temp_media = []
count_critico = []

for i in range(len(temp_salas)):
    media = 0.0
    critico_sala = 0

    for j in range(len(temp_salas[i])):
        media += temp_salas[i][j]
        if temp_salas[i][j] >= 33:
            critico_sala += 1

    temp_media.append(media / len(temp_salas[i]))
    count_critico.append(critico_sala)  # Adiciona o total da sala à lista

    print(f"Sala {i + 1} - Média: {temp_media[i]} | Críticos: {count_critico[i]}")
