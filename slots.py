import random

ACCOUNTS_FILE = "accounts.txt"

def load_accounts():
    accounts = {}
    try:
        f = open(ACCOUNTS_FILE, "r")
        for line in f:
            parts = line.strip().split(" ")
            if len(parts) >= 2:
                username = parts[0]
                password = parts[1]
                coins = int(parts[2]) if len(parts) >= 3 else 50
                accounts[username] = {"password": password, "coins": coins}
        f.close()
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts):
    f = open(ACCOUNTS_FILE, "w")
    for username, data in accounts.items():
        f.write(f"{username} {data['password']} {data['coins']}\n")
    f.close()

def login():
    while True:
        choice = input("Login or Create Account? (login/create): ").strip().lower()

        if choice == "create":
            accounts = load_accounts()
            username = input("Choose a username: ").strip()
            if " " in username:
                print("Username cannot contain spaces.")
                continue
            if username in accounts:
                print("Username already taken. Try a different one.")
                continue
            password = input("Choose a password: ").strip()
            if " " in password:
                print("Password cannot contain spaces.")
                continue
            accounts[username] = {"password": password, "coins": 50}
            save_accounts(accounts)
            print(f"Account created! Welcome, {username}!")
            return username, 50

        elif choice == "login":
            accounts = load_accounts()
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if username in accounts and accounts[username]["password"] == password:
                saved_coins = accounts[username]["coins"]
                print(f"Welcome back to Lucky Loop, {username}!")
                return username, saved_coins
            else:
                print("Invalid username or password. Try again.")

        else:
            print("Please type 'login' or 'create'.")

username, coins = login()

symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"]

print(f"{coins} 🪙")
print(f"Welcome to 🍀 Lucky Loop 🍀, {username}!")

while True:
    spinning = input("Spin for 5 🪙 ? yes/cash out: ").strip().lower()

    if not ((spinning == "yes" or spinning == "") and coins > 4):
        print(f"You left with {coins} 🪙")
        accounts = load_accounts()
        accounts[username]["coins"] = coins
        save_accounts(accounts)
        print("Coins saved to your account!")
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
