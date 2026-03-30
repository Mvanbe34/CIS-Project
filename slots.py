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
    if spinning == "yes":
        if coins > 4:
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