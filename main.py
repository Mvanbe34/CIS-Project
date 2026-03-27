import random
symbols = ["🍒", "🍋", "🍊", "🍇", "⭐", "🔔", "💎"]
count = 0
while count != 3:
    winner_emojis = random.choice(symbols)
    print(winner_emojis, end=' ')
    count += 1
