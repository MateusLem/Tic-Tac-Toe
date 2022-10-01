# Tic-Tac-Toe

<p align="center"> This project...</p>

# Content

<!--cont-start-->
    * [About](#about)
        * [Reason](#Reason)
        * [Goal](#Goal)
        * [Proposed Rules](#Proposed Rules)
    * [Content](#Content)
        * [Gamemodes](#Gamemodes)
            * [Player vs Player](#Player vs Player)
            * [Player vs Machine (easy)](#Player vs Machine (easy))
        * [Mandatory](#Mandatory)
            * [inicializarTabuleiro](#inicializarTabuleiro)
            * [imprimirTabuleiro](#imprimirTabuleiro )
            * [imprimeMenuPrincipal](#imprimeMenuPrincipal)
            * [leiaCoordenadaLinha](#leiaCoordenadaLinha)
            * [leiaCoordenadaColuna](#leiaCoordenadaColuna)
            * [imprimePontuacao](#imprimePontuacao)
            * [posicaoValida](#posicaoValida)
            * [verificaVencedor](#verificaVencedor)
            * [verificaVelha](#verificaVelha)
            * [modoJogador](#modoJogador)
            * [jogar](#jogar)
            * [jogadaUsuario](#jogadaUsuario)
        * [Personal](#Personal)

    * [More](#more)
<!--cont-end-->

## About
* The board must be a 3X3 matrix;
* Two players must each have one mark (O and X);
* Players play one marking at a time in a position that is empty;
* The match will consist of several games;
* If the game was started by one player and there was a tie, then the game must be started by the other player;
* When winning a game, the winning player gets 1 point;
* The match will end when a player or machine reaches 3 points;
* After that, the program returns to the main menu.
### Reason
* This project was requested as an assessment of the Python subject during the second semester of 2022 of the <a href="https://www.fiap.com.br/?msclkid=21318f39943217618b84ec01f5bc0435">FIAP</a> systems analysis and development course.

### Goal
* The project aimed to work with data manipulation through functions, lists and list of lists (arrays) in Python.

## Content
* The program consists of a menu that allows you to choose between 3 options: <a href="#PvP">Player vs Player</a>, <a href="#PvP">Player vs Machine (easy)</a> and Quit;
* For the purpose, a mix of <a href="#Mandatory">mandatory</a> and <a href="#Personal">personal</a> functions were used.

### Gamemodes
* List of available gamemodes

#### Player vs Player
* In this mode, the player must play against another player.

#### Player vs Machine (easy)
* In this mode, the player must play against the machine;
* As it is the easy mode, the machine has no strategy, that is, it will play randomly in the positions that are available on the board.
<h4 align="center">
        🚧 Functionality Under construction 🚧
</h4>-->

### Mandatory
* List of mandatory functions

#### inicializarTabuleiro
* Function that initializes the board, that is, prepares the board for the move.

#### imprimirTabuleiro
* Function that prints the tic-tac-toe board for the user.

#### imprimeMenuPrincipal
* Function that prints the game's main menu.

#### leiaCoordenadaLinha
* Function without parameters reads and returns the line coordinate to the user.

#### leiaCoordenadaColuna
* Function without parameters reads and returns the column coordinate to the user.

#### imprimePontuacao
* Function that prints the status of the game, that is, the score of each player in the match;
* This function must be called several times each time you start a new game.

#### posicaoValida
* Receives row and column coordinates and checks if that position is valid (that is, if it exists on the board and if that position is empty).

#### verificaVencedor
* Function that checks if there was a winner, be it player 1, player 2 or machine.

#### verificaVelha
* Function that checks if the game ended in a draw.

#### modoJogador
* Function that performs all operations for <a href="#Player vs Player">Player vs Player</a>.

#### jogar
* Function that receives row and column coordinates and exclusively fills the board;
* Assignment on the board can only be done by this function;
* It must be used by the players and the computer;
* The played function only assigns "X" or "O" on the board.

#### jogadaUsuario
* Function that receives the player's coordinates and necessarily calls the <a href="#jogar">jogar</a> function to insert it on the board.



<!--<h4 align="center">
        🚧 READ.ME Under construction 🚧
    </h4>-->
