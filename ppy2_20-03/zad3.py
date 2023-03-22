import getpass
import random

if __name__ == '__main__':
    beats = {
        'k': 'n',
        'n': 'p',
        'p': 'k'
    }
    results = []
    currentRound = 1

    round_number = input("Podaj ilość rund: ")
    while int(round_number) <= 0:
        round_number = input("Podaj ilość rund: ")

    game_mode = input("Podaj tryb gry [0 - komputer; 1 - dwóch graczy]: ")

    while game_mode not in ['0', '1']:
        game_mode = input("Podaj tryb gry [0 - komputer; 1 - dwóch graczy]: ")

    isMultiplayer = (game_mode == '1')

    player1_name = input("Podaj nazwę gracza 1: ")
    player2_name = input(f"Podaj nazwę {'gracza 2' if isMultiplayer else 'dla komputera'}: ")

    for i in range(0, int(round_number)):
        print(f'\nRunda {currentRound}!')
        cpu_choices = ['p', 'k', 'n']

        player1_choice = getpass.getpass(prompt=f"Kolejka {player1_name} [p, k, n]: ") if isMultiplayer else input(f"Kolejka {player1_name} [p, k, n]: ")
        player1_choice = player1_choice[0].lower()

        while player1_choice not in cpu_choices:
            player1_choice = getpass.getpass(prompt=f"Kolejka {player1_name} [p, k, n]: ") if isMultiplayer else input(f"Kolejka {player1_name} [p, k, n]: ")

        player2_choice = getpass.getpass(prompt=f"Kolejka {player2_name} [p, k, n]: ") if isMultiplayer else cpu_choices[random.randint(0, 2)]
        player2_choice = player2_choice[0].lower()

        while player1_choice not in cpu_choices:
            player1_choice = getpass.getpass(prompt=f"Kolejka {player1_name} [p, k, n]: ") if isMultiplayer else input(f"Kolejka {player1_name} [p, k, n]: ")



        if player1_choice == player2_choice:
            print('Remis!')
            results.append('0,0')
        elif beats.get(player1_choice) == player2_choice:
            print(f'{player1_name} wygrywa rundę!')
            results.append('1,0')
        else:
            print(f'{player2_name} wygrywa rundę!')
            results.append('0,1')

        currentRound += 1

    player1_count = 0
    player2_count = 0

    for result in results:
        res = result.split(',')
        player1_count += int(res[0])
        player2_count += int(res[1])

    if player1_count != player2_count:
        print(f'\n\nWygrywa {player1_name if player1_count > player2_count else player2_name}!')
    else:
        print('\n\nRemis!')

    print(f'Wyniki [{player1_name} : {player2_name}]')

    for index, result in enumerate(results):
        res = result.split(',')
        print(f'Runda {index+1}: {res[0]} : {res[1]}')

    print(f'\nOstateczny wynik: {player1_count} : {player2_count}')
