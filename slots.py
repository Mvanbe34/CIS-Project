import random
with open("accounts.txt", "a") as file:
    user_input=input('Login or Create Account? (login/create): ')
    if user_input == 'create':
        create_account=input('type in a usernme and password you would like. (username_password): ')
        with open("account.txt", "a") as f:
            f.write(create_account)
    elif user_input == 'login':
        account_login= input('enter username:password: ')
        with open('account.txt', 'r') as f:
            content = f.read()
            if account_login in content:
                print("Welcome back to Lucky Loop",account_login)
            else:
                print("Account not found. Try again")

accounts = {}


symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"]
coins = 50

print(f"{coins} 🪙")
print("Welcome to 🍀 Lucky Loop 🍀")

while True:
    spinning = input("Spin for 5 🪙 ? yes/cash out: ").strip().lower()

    if not ((spinning == "yes" or spinning == "") and coins > 4):
        print(f"You left with {coins} 🪙")
        break

    coins -= 5
    print("🍀Lucky Loop🍀")

    board = [random.choice(symbols) for _ in range(9)]

    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2], sep="  ")

    if board[0] == board[1] == board[2]:
        coins += 15
        print("Top Row +15 🪙")

    if board[3] == board[4] == board[5]:
        if board[3] == "💎":
            coins += 500
            print("MEGA JACKPOT!!!!!!!!! +500 🪙")
        else:
            coins += 50
            print("Middle Row +50 🪙")

    if board[6] == board[7] == board[8]:
        coins += 15
        print("Bottom Row +15 🪙")

    if board[0] == board[3] == board[6]:
        coins += 10
        print("First Column +10 🪙")

    if board[1] == board[4] == board[7]:
        coins += 10
        print("Second Column +10 🪙")

    if board[2] == board[5] == board[8]:
        coins += 10
        print("Third Column +10 🪙")

    if board[0] == board[4] == board[8]:
        coins += 20
        print("Main Diagonal +20 🪙")

    if board[2] == board[4] == board[6]:
        coins += 20
        print("Anti Diagonal +20 🪙")

    print(f"{coins} 🪙")

'''
import random
symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"]
count = 0
counts = 0
points_checker = []
coins = 50
print(f"{coins} 🪙")
flag = True
print("Welcome to 🍀 Lucky Loop 🍀")
while flag == True:
    spinning = input("Spin for 5 🪙 ? yes/cash out: ")
    if (spinning == "yes" or spinning == "") and coins > 4:
        coins -= 5
        print("🍀Lucky Loop🍀")
        while counts != 3:
            while count != 3:
                winner_emoji = random.choice(symbols)
                print(winner_emoji, end='  ')
                points_checker.append(winner_emoji)
                count += 1
            count = 0
            print()
            counts += 1
        if points_checker[0] == points_checker[1] == points_checker[2]:
            coins += 15
            print("Top Row +15 🪙")
        if points_checker[3] == points_checker[4] == points_checker[5]:
            if points_checker[3] == "💎":
                coins += 500
                print("MEGA JACKPOT!!!!!!!!! +500 🪙")
            else:
                coins += 50
                print("Middle Row +50 🪙")
        if points_checker[6] == points_checker[7] == points_checker[8]:
            coins += 15
            print("Bottom Row +15 🪙")
        if points_checker[0] == points_checker[3] == points_checker[6]:
            coins += 10
            print("First Column +10 🪙")
        if points_checker[1] == points_checker[4] == points_checker[7]:
            coins += 10
            print("Second Column +10 🪙")
        if points_checker[2] == points_checker[5] == points_checker[8]:
            coins += 10
            print("Third Column +10 🪙")
        if points_checker[0] == points_checker[4] == points_checker[8]:
            coins += 20
            print("Main Diagonal +20 🪙")
        if points_checker[2] == points_checker[4] == points_checker[6]:
            coins += 10
            print("Anti Diagonal +20 🪙")
        print(f"{coins} 🪙")
        points_checker = []
        count = 0
        counts = 0
    else:
        print(f"You left with {coins} 🪙")
        flag = False
'''