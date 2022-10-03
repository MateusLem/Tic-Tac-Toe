# Tic-Tac-Toe

# Content
* [About](#about)
    * [Reason](#Reason)
    * [Goal](#Goal)
* [Content](#Content)
    * [Gamemodes](#Gamemodes)
        * [Player vs Player](#Player-vs-Player)
        * [Player vs Machine (easy)](#Player-vs-Machine-easy)
    * [Mandatory](#Mandatory)
        * [inicializarTabuleiro](#inicializarTabuleiro)
        * [imprimirTabuleiro](#imprimirTabuleiro)
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
        * [out](#out)
        * [valida](#valida)
        * [coordenadas](#coordenadas)
        * [reset](#reset)
        * [restart](#restart)
        * [programa](#programa)
* [More](#More)
    * [Tecnologies](#Tecnologies)
    * [Original Language](#Original-Language)
    * [Latest Update](#Latest-Update) 
* [Contact Me](#Contact-Me)

# About
* The board must be a 3X3 matrix;
* Two players must each have one mark (O and X);
* Players play one marking at a time in a position that is empty;
* The match will consist of several games;
* If the game was started by one player and there was a tie, then the game must be started by the other player;
* When winning a game, the winning player gets 1 point;
* The match will end when a player or machine reaches 3 points;
* After that, the program returns to the main menu.

## Reason
* This project was requested as an assessment of the Python subject during the second semester of 2022 of the [FIAP](https://www.fiap.com.br/?msclkid=21318f39943217618b84ec01f5bc0435) systems analysis and development course.
## Goal
* The project aimed to work with data manipulation through functions, lists and list of lists (arrays) in Python.
# Content
* The program consists of a menu that allows you to choose between 3 options: [Player vs Player](#Player-vs-Player), [Player vs Machine (easy)](#Player-vs-Machine-easy);
* For this purpose, a mix of [mandatory](#Mandatory) and [personal](#Personal) functions were used.

## Gamemodes
List of available gamemodes:
### Player-vs-Player
* In this mode, the player must play against another player.
### Player-vs-Machine-easy
* In this mode, the player must play against the machine;
* As it is the easy mode, the machine has no strategy, that is, it will play randomly in the positions that are available on the board.
<h4 align="center">🚧 Functionality Under Construction 🚧</h4>

## Mandatory
List of mandatory functions:
### inicializarTabuleiro
* Function that initializes the board, that is, prepares the board for the move.
### imprimirTabuleiro
* Function that prints the tic-tac-toe board for the user.
### imprimeMenuPrincipal
* Function that prints the game's main menu.
### leiaCoordenadaLinha
* Function without parameters reads and returns the line coordinate to the user.
### leiaCoordenadaColuna
* Function without parameters reads and returns the column coordinate to the user.
### imprimePontuacao
* Function that prints the status of the game, that is, the score of each player in the match;
* This function must be called several times each time you start a new game.
### posicaoValida
* Receives row and column coordinates and checks if that position is valid (that is, if it exists on the board and if that position is empty).
### verificaVencedor
* Function that checks if there was a winner, be it player 1, player 2 or machine.
### verificaVelha
* Function that checks if the game ended in a draw.
### modoJogador
* Function that performs all operations for [Player vs Player](#Player-vs-Player) gamemode.
### jogar
* Function that receives row and column coordinates and exclusively fills the board;
* Assignment on the board can only be done by this function;
* It must be used by the players and the computer;
* The played function only assigns "X" or "O" on the board.
### jogadaUsuario
* Function that receives the player's coordinates and necessarily calls the [jogar](#jogar) function to insert it on the board.

## Personal
List of personal functions:
### out
* Function that fix the Out Of Range error.
### valida
* Function that identifies if there is an Out Of Range or occupied position error.
#### coordenadas
* Function that calls the functions [leiaCoordenadaLinha](#leiaCoordenadaLinha) and [leiaCoordenadaColuna](#leiaCoordenadaColuna) to set the coordinates.
### reset
* Function that resets the round.
### restart
* Function that resets the values of "p1", "p2", "rodada" and "matriz" at the end of the game.
### programa
* Main program function.

# More
More information about his project:
## Tecnologies 🛠️
* Used tools for this project:
    - [Python](https://www.python.org/) ([PyCharm](https://www.jetbrains.com/pycharm/))

## Original-Language
* Portuguese - Brazil
## Latest-Update
* Oct/01/2022
---
Made with tenacity by Mateus Leme
## Contact-Me
<h3>
<img alt="LinkedIn" title="LinkedIn" src="./github/img/linkedin.png" width="15vw" height="15vh">
<a href="https://www.linkedin.com/in/mateus-da-costa-leme-35a5ab235/">LinkedIn</a>
</h3>


<!--<h4 align="center">
        🚧 READ.ME Under construction 🚧
    </h4>-->
