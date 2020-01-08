import random

def playHangman():
    playerScore = 0
    CPUScore = 0

    while playerScore < 3 and CPUScore < 3:
        playerSelection = input("(R)ock, (P)aper, or (S)cissors?")
        CPUSelection = random.choice('rps')

        if playerSelection.lower() == 'r':
            if CPUSelection == 'p':
                print("CPU throws paper!")
                CPUScore += 1
                print("You:", playerScore, " CPU:", CPUScore)
            elif CPUSelection == 's':
                print("CPU throws scissors!")
                playerScore += 1
                print("You:", playerScore, " CPU:", CPUScore)
            else:
                print("You:", playerScore, " CPU:", CPUScore)
                print("CPU throws rock! TIE!")

        if playerSelection.lower() == 'p':
            if CPUSelection == 'r':
                print("CPU throws rock!")
                playerScore += 1
                print("You:", playerScore, " CPU:", CPUScore)
            elif CPUSelection == 's':
                print("CPU throws scissors!")
                CPUScore += 1
                print("You:", playerScore, " CPU:", CPUScore)
            else:
                print("You:", playerScore, " CPU:", CPUScore)
                print("CPU throws paper! TIE!")

        if playerSelection.lower() == 's':
            if CPUSelection == 'p':
                print("CPU throws paper!")
                playerScore += 1
                print("You:", playerScore, " CPU:", CPUScore)
            elif CPUSelection == 'r':
                print("CPU throws rock!")
                CPUScore += 1
                print("You:", playerScore, " CPU:", CPUScore)
            else:
                print("You:", playerScore, " CPU:", CPUScore)
                print("CPU throws scissors! TIE!")

    if playerScore == 3:
        print("Congratulations! You win!")
    else:
        print("CPU wins! Better luck next time!")

playHangman()