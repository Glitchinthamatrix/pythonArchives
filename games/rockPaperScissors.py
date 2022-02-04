from platform import machine
import random

def who_wins(human,machine):
    if (human=="S" and machine=="P") or (human=="R" and machine=='S') or (human=="P" and machine=='R'):
        return True


def play():
    human_inp=str(input("S for Scissors, R for Rock, P fpr Paper, which one do you choose? "))
    options=['S','P','R']
    machine_inp=random.choice(options)
    if human_inp not in options:
        print("Don't choose anything other than S, R or P (Capitals)")
    else:
        if machine_inp == human_inp:
            print(f"it's a tie, machine input: {machine_inp}, human input: {human_inp}")
        else:
            human_won=who_wins(human_inp,machine_inp)
            print(f"machine: {machine_inp}, human: {human_inp}")
            print("You won!" if human_won else "You lost to a pile of metals")
play()
