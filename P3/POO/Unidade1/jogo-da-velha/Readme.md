Olá, fiz este projeto no 3º período na matéria de Programação Orientada a Objetos. A seguir, vou comentar sobre cada classe e o que ela faz no projeto.

Classe JogoDaVelha.java:
É a classe que contém o método main, ou seja, a classe principal do projeto. Nela que a aplicação será iniciada. Tentei deixar ela mais enxuta ou "clean" possível, por isso não declarei variáveis, métodos, etc.

Classe Tabuleiro.java:
É a classe que constrói o tabuleiro, o desenha, e também faz a checagem, para ver se a posição selecionada por jogador 'x' está ou não preenchida.

Classe Jogo.java:
Através de variáveis, essa classe irá criar um tabuleiro, números para controlar de quem será a vez de jogar, dois jogadores e um Scanner para receber a entrada dos jogadores humanos.

Classe Jogador.java:
Nessa classe, vão ter 2 tipos de jogadores: humano e computador, com seus métodos de jogar diferentes.

Classe Humano.java:
A classe Humano herda a classe Jogador, e cada objeto criado recebe o número 1 ou 2, que vai identificar como jogador 1 ou jogador 2, para passar a informação de quem é o jogador da vez.

Classe Computador.java:
Assim como na classe Humano, a classe Computador herda a classe abstrata Jogador.
Por enquanto ela não faz nada, pois não consegui implementar a inteligência artificial, mas em breve, estarei implementando e atualizando o game.