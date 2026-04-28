import random

# path to the flat-file database that stores all user accounts
accounts_file = "accounts.txt"

def load_accounts():
    # reads accounts_file and returns a dict of {username: {password, coins}}
    accounts = {}
    try:
        f = open(accounts_file, "r")
        for line in f:
            # each line is: username password coins
            parts = line.strip().split(" ")
            if len(parts) >= 2:
                username = parts[0]
                password = parts[1]
                # default to 50 coins if the coins field is missing
                coins = int(parts[2]) if len(parts) >= 3 else 50
                accounts[username] = {"password": password, "coins": coins}
        f.close()
    except FileNotFoundError:
        # first run — no file yet, just return an empty dict
        pass
    return accounts

def save_accounts(accounts):
    # overwrites accounts_file with the current state of all accounts
    f = open(accounts_file, "w")
    for username, data in accounts.items():
        f.write(f"{username} {data['password']} {data['coins']}\n")
    f.close()

def login():
    # loops until the user successfully logs in or creates an account
    while True:
        choice = input("Login or Create Account? (login/create): ").strip().lower()

        if choice == "create":
            accounts = load_accounts()
            username = input("Choose a username: ").strip()
            # spaces would break the space-delimited file format
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
            # new accounts start with 50 coins
            accounts[username] = {"password": password, "coins": 50}
            save_accounts(accounts)
            print(f"Account created! Welcome, {username}!")
            return username, 50

        elif choice == "login":
            accounts = load_accounts()
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if username in accounts and accounts[username]["password"] == password:
                # restore the coin balance from the last session
                saved_coins = accounts[username]["coins"]
                print(f"Welcome back to Lucky Loop, {username}!")
                return username, saved_coins
            else:
                print("Invalid username or password. Try again.")

        else:
            print("Please type 'login' or 'create'.")

# authenticate and get starting coin balance
username, coins = login()

# all possible symbols that can appear on the board
symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"]

print(f"{coins} 🪙")
print(f"Welcome to 🍀 Lucky Loop 🍀, {username}!")

while True:
    spinning = input("Spin for 5 🪙 ? yes/cash out: ").strip().lower()

    # exit if the player types anything other than "yes"/enter, or runs out of coins
    if not ((spinning == "yes" or spinning == "") and coins > 4):
        print(f"You left with {coins} 🪙")
        # persist the final coin balance before quitting
        accounts = load_accounts()
        accounts[username]["coins"] = coins
        save_accounts(accounts)
        print("Coins saved to your account!")
        break

    # deduct spin cost before revealing the board
    coins -= 5
    print("🍀Lucky Loop🍀")

    # generate a 3x3 grid of random symbols (stored as a flat 9-element list)
    board = [random.choice(symbols) for _ in range(9)]

    # print the board in rows of 3
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2], sep="  ")

    # --- payout checks ---

    # top row win
    if board[0] == board[1] == board[2]:
        coins += 15
        print("Top Row +15 🪙")

    # middle row win — diamonds trigger the mega jackpot
    if board[3] == board[4] == board[5]:
        if board[3] == "💎":
            coins += 500
            print("MEGA JACKPOT!!!!!!!!! +500 🪙")
        else:
            coins += 50
            print("Middle Row +50 🪙")

    # bottom row win
    if board[6] == board[7] == board[8]:
        coins += 15
        print("Bottom Row +15 🪙")

    # column wins (smaller payout than rows)
    if board[0] == board[3] == board[6]:
        coins += 10
        print("First Column +10 🪙")

    if board[1] == board[4] == board[7]:
        coins += 10
        print("Second Column +10 🪙")

    if board[2] == board[5] == board[8]:
        coins += 10
        print("Third Column +10 🪙")

    # diagonal wins
    if board[0] == board[4] == board[8]:
        coins += 20
        print("Main Diagonal +20 🪙")

    if board[2] == board[4] == board[6]:
        coins += 20
        print("Anti Diagonal +20 🪙")

    print(f"{coins} 🪙")
