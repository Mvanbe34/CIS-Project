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
                try:
                    coins = int(parts[2]) if len(parts) >= 3 else 50
                except ValueError:
                    coins = 50
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

class Slot_Machine:
    def __init__(self, name, spin_cost, symbols):
        self.name = name
        self.spin_cost = int(spin_cost)
        self.symbols = symbols
    def display_info(self):
        print(self.name)
        print(f"Spin Cost: {self.spin_cost}")
        print(f"Symbols: {self.symbols}")
    def can_afford(self):
        if coins >= self.spin_cost:
            print("You can afford to spin!")
        else:
            print("You can not afford to spin.")
    def check_win(self, first, second, third, payout, label):
        # returns winnings if the three board positions all match, else 0
        if board[first] == board[second] == board[third]:
            won = payout * m
            print(f"{label} +{won} 🪙")
            return won
        return 0

machine1 = Slot_Machine("Lucky Loop 🍀", 5, ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"])
machine2 = Slot_Machine("High Roller 👑", 15, ["🦁", "👑", "💰", "🎰", "🌟", "🔥"])

print(f"{coins} 🪙")
print(f"Welcome, {username}! Pick your machine:")
print("1 - Lucky Loop 🍀 (5 🪙 per spin)")
print("2 - High Roller 👑 (15 🪙 per spin)")

# let the player choose which machine to play
while True:
    pick = input("Enter 1 or 2: ").strip()
    if pick == "1":
        machine = machine1
        break
    elif pick == "2":
        machine = machine2
        break
    else:
        print("Please enter 1 or 2.")

print(f"Welcome to {machine.name}, {username}!")
machine.display_info()
machine.can_afford()

while True:
    spinning = input(f"Spin for {machine.spin_cost} 🪙 ? yes/cash out: ").strip().lower()

    # exit if the player types anything other than "yes"/enter, or runs out of coins
    if not ((spinning == "yes" or spinning == "") and coins >= machine.spin_cost):
        print(f"You left with {coins} 🪙")
        # persist the final coin balance before quitting
        accounts = load_accounts()
        accounts[username]["coins"] = coins
        save_accounts(accounts)
        print("Coins saved to your account!")
        break

    # deduct spin cost before revealing the board
    coins -= machine.spin_cost
    print(machine.name)

    # generate a 3x3 grid of random symbols (stored as a flat 9-element list)
    board = [random.choice(machine.symbols) for _ in range(9)]

    # print the board in rows of 3
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2], sep="  ")

    # --- payout checks ---
    # scale all payouts proportionally to the spin cost (base cost is 5)
    m = machine.spin_cost // 5

    coins += machine.check_win(0, 1, 2, 15, "Top Row")

    # middle row win — jackpot symbol triggers the mega jackpot
    if board[3] == board[4] == board[5]:
        if board[3] == machine.symbols[5]:
            coins += 500 * m
            print(f"MEGA JACKPOT!!!!!!!!! +{500 * m} 🪙")
        else:
            coins += machine.check_win(3, 4, 5, 50, "Middle Row")

    coins += machine.check_win(6, 7, 8, 15, "Bottom Row")
    coins += machine.check_win(0, 3, 6, 10, "First Column")
    coins += machine.check_win(1, 4, 7, 10, "Second Column")
    coins += machine.check_win(2, 5, 8, 10, "Third Column")
    coins += machine.check_win(0, 4, 8, 20, "Main Diagonal")
    coins += machine.check_win(2, 4, 6, 20, "Anti Diagonal")

    print(f"{coins} 🪙")
