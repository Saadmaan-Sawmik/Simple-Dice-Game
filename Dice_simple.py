import random

def main():

    round = 1
    player1_won = 0
    player2_won = 0

    while round < 4:
        print('round ' + str(round))
        player1 = dice_roll()
        player2 = dice_roll()
        print("first  player {}".format(player1))
        print("second player {}".format(player2))

        if player2 > player1:
            player2_won += 1
            print('player 2 won')
        elif player1 > player2:
            player1_won += 1
            print('player 1 won')
        else:
            print('Draw')
        print()

        round += 1

    if player1_won > player2_won:
        print('Player 1 won the match')
    elif player2_won > player1_won:
        print('Player 2 won the match')
    else:
        print("Draw")


def dice_roll():
    dice_num = random.randint(1, 6)
    return dice_num

main()

