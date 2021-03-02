from random import randint

value = randint(1, 3)
player = randint(1, 3)

papierplayer = False
papierbot = False
pierreplayer = False
pierrebot = False
ciseauplayer = False
ciseaubot = False

if value == 1:
    print("rock")
    pierrebot = True
elif value == 2:
    print("paper")
    papierbot = True
elif value == 3:
    print("scissor")
    ciseaubot = True

if player == 1:
    print("rock")
    pierreplayer = True
elif player == 2:
    print("paper")
    papierplayer = True
elif player == 3:
    print("scissor")
    ciseauplayer = True

if pierreplayer and ciseaubot and not papierbot:
    print("bot1 won")
    winner = "player"
elif papierplayer and pierrebot and not ciseaubot:
    print("bot1 won")
    winner = "player"
elif ciseauplayer and papierbot and not pierrebot:
    print("bot1 won")
    winner = "player"
elif pierrebot and ciseauplayer and not papierplayer:
    print("bot2 won")
    winner = "bot"
elif papierbot and pierreplayer and not ciseauplayer:
    print("bot2 won")
    winner = "bot"
elif ciseaubot and papierplayer and not pierreplayer:
    print("bot2 won")
    winner = "bot"
elif player == value:
    print("tie")



