import random

def get_user_choice():
    user_choice = input("Elige piedra (r), papel (p) o tijeras (s): ")
    if user_choice in ['r', 'p', 's']:
        return user_choice
    else:
        print("Opción inválida. Intenta de nuevo.")
        return get_user_choice()

def get_computer_choice():
    computer_choice = random.choice(['r', 'p', 's'])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Tu elección:", user_choice)
    print("Elección de la computadora:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

play_game()
