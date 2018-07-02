lottery_players = []

print("===============================")
print("Welcome to Kenzie's Lucky Draw")
print("===============================")


def print_players_list():
    print()
    print("Here are the list of players and their lucky numbers! Goodluck!")
    print("================================================================")
    for plays in lottery_players:
        print(plays)
    print("================================================================")

def generate_lucky_number():
    lottery_number_result = input("Please enter the Lottery Lucky Number Result: ")
    for plays in lottery_players:
       for number in plays['Lucky_Numbers']:
           if(lottery_number_result == number):
               print("{} is a winner!".format(plays["Player_Name"]))

add_player = True
while add_player == True:
    print()
    player_name = input("Enter the name of the player: ") 
    player_numbers = input("Enter lucky numbers separated by ',': ")
    lottery_players.append({
        'Player_Name': player_name,
        'Lucky_Numbers': player_numbers.split(",")
    })
    print("===============================")
    print()
    player_asnwer = input("Would you like to add another player? y/n: ")
    if(player_asnwer == 'n'):
        add_player = False
        print_players_list()
        generate_lucky_number()
