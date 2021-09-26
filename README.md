# Jogo ElementPo

É um jogo que consiste em algumas regras básicas para se jogar.

1. Existem 20 cartas no baralho dividida em 4 elementos: Água, Fogo, Ar e Terra.
2. As cartas de cada elemento são únicas e tem 5 níveis: Fogo 1, Fogo 2, Fogo 3, etc.
3. Os jogadores devem completar as posições de um jogo da velha comum, vencendo batalhas na posições do campo.
4.Em todas as batalhas existe a verificação do elemento, sendo que ao elemento ser predominante tem seu nível multiplicado por 2. Sendo: Fogo > Ar; Ar > Terra; Terra > Água e Água > Fogo.
5. Caso não tenha um elemento predominante, é utilizado o nível das cartas comum. Ex: Fogo 5 > Terra 4.
6. Isso acontece sempre que há escolha de campo de batalha em comum. Caso escolha um campo que não tenha outra carta, não acontece a batalha neste turno.

Para conseguir rodar o jogo, são necessárias as seguintes configurações:

1. Ter instalado em seu computador o *Python 3.9.6*.
2. Instalar a biblioteca PyQT5. Para isso, executar o comando *pip install PyQt5*.
3. Entrar na pasta do jogo onde contém o arquivo main.py - *elementoPo/src/*.
4. Executar o comando *python main.py*. 

Divirtam-se!
