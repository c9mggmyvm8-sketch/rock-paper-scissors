computer1 =0
player1= 0

import random
def get_computer_choice():
    computer_choice = ["камень", "ножницы", "бумага"]
    return random.choice(computer_choice)

def determine_winner(player, computer):
    global computer1
    global player1
    if player == computer:
        print(f"Компьютер: {computer}")
        print("Ничья: Никому не присуждается балл")
        print(f"Игрок: {player1}, Компьютер: {computer1}")
    elif player == "камень" and computer =="ножницы":
        print(f"Компьютер: {computer}")
        print("Вы выиграли, Вам присуждается балл")
        player1 +=1
        print(f"Игрок: {player1}, Компьютер: {computer1}")
    elif player == "ножницы" and computer == "бумага":
        print(f"Компьютер: {computer}")
        print("Вы выиграли, Вам присуждается балл")
        player1 +=1
        print(f"Игрок: {player1}, Компьютер: {computer1}")
    elif player == "бумага" and computer == "камень":
        print(f"Компьютер: {computer}")
        print("Вы выиграли, Вам присуждается балл")
        player1 +=1
        print(f"Игрок: {player1}, Компьютер: {computer1}")
    else:
        print(f"Компьютер: {computer}")
        print("Выиграл компьютер, Компьютеру присуждается балл")

        computer1 += 1
        print(f"Игрок: {player1}, Компьютер: {computer1}")
никто_не_выиграл = True
while никто_не_выиграл:
    player=input("Введите камень, ножницы, бумага: ")
    computer=get_computer_choice()
    determine_winner(player, computer)
    if player1 == 3:
        print("Игрок выиграл")
        print(f"Игрок: {player1}, Компьютер: {computer1}")
        никто_не_выиграл = False
    if computer1 == 3:
        print("Компьютер выиграл")
        print(f"Игрок: {player1}, Компьютер: {computer1}")

        никто_не_выиграл = False