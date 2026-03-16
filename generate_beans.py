import random
import csv

NUM_BEANS = 1000

# Ograniczenia projektu
MAX_WEIGHT = 250
MAX_BUDGET = 40

countries = [
    "Etiopia", "Brazylia", "Kolumbia", "Indie",
    "Wietnam", "Gwatemala", "Kenia", "Peru",
    "Honduras", "Tanzania"
]

with open("coffee_beans.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "weight", "price", "intensity", "acidity"])

    for i in range(NUM_BEANS):

        name = random.choice(countries)
        intensity = random.randint(1, 10)
        acidity = random.randint(1, 10)

        # 50% poprawnych
        if i < NUM_BEANS // 2:
            weight = random.randint(10, MAX_WEIGHT)
            price = random.randint(1, MAX_BUDGET)

        # 50% całkowicie niepoprawnych (oba warunki przekroczone)
        else:
            weight = random.randint(MAX_WEIGHT + 1, 400)
            price = random.randint(MAX_BUDGET + 1, 100)

        writer.writerow([name, weight, price, intensity, acidity])

print("✅ 50% ziaren całkowicie przekracza wagę i budżet")