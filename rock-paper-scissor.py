from random import randint

seed(1)
value = randint(1, 3)

papierplayer = False
papierbot = False
pierreplayer = False
pierrebot = False
ciseauplayer = False
ciseaubot = False

winner = "no one"

player = input("rock paper scissor: ")

if player == "rock":
    subplayer = 1
    pierreplayer = True
if player == "paper":
    subplayer = 2
    papierplayer = True
if player == "scissor":
    subplayer = 3
    ciseauplayer = True

if value == 1:
    print("rock")
    pierrebot = True
if value == 2:
    print("paper")
    papierbot = True
if value == 3:
    print("scissor")
    ciseaubot = True

if pierreplayer and ciseaubot and not papierbot:
    print("u won")
    winner = "player"
if papierplayer and pierrebot and not ciseaubot:
    print("u won")
    winner = "player"
if ciseauplayer and papierbot and not pierrebot:
    print("u won")
    winner = "player"

if pierrebot and ciseauplayer and not papierplayer:
    print("u lost")
    winner = "bot"
if papierbot and pierreplayer and not ciseauplayer:
    print("u lost")
    winner = "bot"
if ciseaubot and papierplayer and not pierreplayer:
    print("u lost")
    winner = "bot"


