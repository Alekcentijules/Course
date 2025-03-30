import random

fill_percentage = random.random() * 100

print(f"Fill percentage: {fill_percentage:.2f}% \n")



import random

target = random.randrange(1, 11, 2)

print(f"Target: {target} \n")



import random

cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6"]
random.shuffle(cards)

print(f"Mixed deck: {cards} \n")



import random

fruits = ["Blackberry", "Dragon Fruit", "Banana", "Kokos"]
weights = [11, 22, 34, 64]
participants = ["Jack", "Johny", "Glosgo", "Tartaran", "Omletti"]
team = random.sample(participants, 4)

print(f"Random fruit: {random.choice(fruits)}")
print(f"Random fruit: {random.choices(fruits, weights, k=2)}")
print(f"Team: {team}")



import random

price = random.uniform(0, 100)

print(f"Random price: {price:.2f}")