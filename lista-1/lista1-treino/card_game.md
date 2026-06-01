A. Card Game
Enunciado
Suneet e Slavic jogam um jogo de cartas.
As regras do jogo são as seguintes:

Cada carta tem um valor inteiro entre 1 e 10.
Cada jogador recebe 2 cartas que estão viradas para baixo (então o jogador não sabe quais são suas cartas).O jogo é baseado em turnos e consiste exatamente em dois turnos. Em uma rodada, ambos os jogadores escolhem uma carta aleatória ainda não virada e a viram. O jogador que virar uma carta com um número estritamente maior vence a rodada. Em caso de igualdade, ninguém vence a rodada.
Um jogador vence o jogo se ele vencer a maioria das rodadas (ou seja, um número estritamente maior que o outro jogador). Em caso de igualdade, ninguém vence o jogo. Como Suneet e Slavic não são melhores amigos, você precisa calcular o número de maneiras que o jogo pode acontecer para que Suneet acabe como o vencedor.Para uma melhor compreensão, por favor verifique a seção de notas.
Entrada
A primeira linha contém um inteiro t (1 ≤ t ≤ 
10ˆ4) — o número de casos de teste.
A primeira e única linha de cada caso de teste contém 4 inteiros 
a1,a2,b1,b2(1≤a1,a2,b1,b2≤10), onde 
a1 e 
a2 representam as cartas que Suneet tem, e 
b1 e 
b2 representam as cartas que Slavic tem, respectivamente.

Output
Para cada caso de teste, imprima um único inteiro — o número de jogos que Suneet venceria considerando todos os jogos possíveis.

Note
Considere o primeiro caso de teste, onde Slavic começa com as cartas que têm os valores 2 e 6, e Suneet começa com as cartas que têm os valores 3 e 8. O jogo pode acontecer de 4 maneiras diferentes:

Suneet vira a carta 3 e Slavic vira a carta 2. Suneet vence a primeira rodada. Em seguida, Suneet vira a carta 8 e Slavic vira a carta 6. Suneet vence a segunda rodada também. Como Suneet venceu 2 rodadas, ele vence o jogo.
Suneet vira a carta 3 e Slavic vira a carta 6. Slavic vence a primeira rodada. Em seguida, Suneet vira a carta 8 e Slavic vira a carta 2. Suneet vence a segunda rodada. Ninguém vence, pois ambos os jogadores venceram a mesma quantidade de rodadas.
Suneet vira a carta 8 e Slavic vira a carta 6. Suneet vence a primeira rodada. Em seguida, Suneet vira a carta 3 e Slavic vira a carta 2. Suneet vence a segunda rodada também. Como Suneet venceu 2 rodadas, ele vence o jogo. Suneet vira a carta 8 e Slavic vira a carta 2. Suneet vence a primeira rodada. Em seguida, Suneet vira a carta 3 e Slavic vira a carta 6. Slavic vence a rodada. Ninguém vence, pois ambos os jogadores venceram a mesma quantidade de rodadas.
Exemplos
Exemplo 1:

Entrada:

5
3 8 2 6
1 1 1 1
10 10 2 2
1 1 10 10
3 8 7 2
Saída:

2
0
4
0
2