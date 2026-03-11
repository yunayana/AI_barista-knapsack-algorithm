import random


# Parametry

maxWeight = 250
maxBudget = 40
HMS = 5       # liczba rozwiązań w pamięci harmonii
HMCR = 0.7    # 70% wybieramy z pamięci, 30% losowo
iterations = 50  # liczba iteracji algorytmu


# Klasa ziarna

class CoffeeBean:
    def __init__(self, weight, price, intensity, acidity):
        self.weight = weight
        self.price = price
        self.intensity = intensity
        self.acidity = acidity


# Stała baza ziaren

beans = [
    CoffeeBean(50, 8, 9, 6),
    CoffeeBean(40, 5, 6, 3),
    CoffeeBean(70, 10, 8, 7),
    CoffeeBean(30, 6, 4, 5),
    CoffeeBean(60, 7, 7, 6),
    CoffeeBean(80, 11, 10, 8),
    CoffeeBean(20, 4, 3, 4),
    CoffeeBean(45, 6, 5, 7),
    CoffeeBean(35, 5, 6, 4),
    CoffeeBean(55, 9, 8, 5)
]

 
# Funkcja oceny rozwiązania

def evaluate(solution):
    total_weight = 0
    total_price = 0
    score = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            bean = beans[i]
            total_weight += bean.weight
            total_price += bean.price
            score += bean.intensity + bean.acidity
   
    if total_weight > maxWeight or total_price > maxBudget:
        return 0
    return score

# Tworzenie losowego rozwiązania

def random_solution():
    return [random.randint(0,1) for _ in range(len(beans))]


# Tworzenie nowego rozwiązania według HMCR

def create_solution(HM):
    solution = []
    for i in range(len(beans)):
        if random.random() < HMCR:   # wybór z pamięci harmonii
            selected_solution = random.choice(HM)
            solution.append(selected_solution[i])
        else:                         # losowo
            solution.append(random.randint(0,1))
    return solution


# Inicjalizacja pamięci harmonii
 
HM = [random_solution() for _ in range(HMS)]
HM_scores = [evaluate(sol) for sol in HM]


# Główna pętla Harmony Search

for _ in range(iterations):
    new_sol = create_solution(HM)
    new_score = evaluate(new_sol)

    min_score = min(HM_scores)
    if new_score > min_score:
        min_index = HM_scores.index(min_score)
        HM[min_index] = new_sol
        HM_scores[min_index] = new_score


# Wybór najlepszego rozwiązania
 
best_index = HM_scores.index(max(HM_scores))
best_solution = HM[best_index]

 
# Wyświetlanie wyników

print("\nDostępne ziarna kawy:\n")
for i, bean in enumerate(beans):
    print(f"ID:{i} | Waga:{bean.weight} | Cena:{bean.price} | Intensywność:{bean.intensity} | Kwasowość:{bean.acidity}")

print("\nNajlepsze rozwiązanie:", best_solution)

# Wyświetlenie szczegółów mieszanki
total_weight = 0
total_price = 0
total_score = 0
print("\nWybrane ziarna:")
for i in range(len(best_solution)):
    if best_solution[i] == 1:
        bean = beans[i]
        print(f"Ziarno {i} | Waga:{bean.weight} | Cena:{bean.price} | Intensywność:{bean.intensity} | Kwasowość:{bean.acidity}")
        total_weight += bean.weight
        total_price += bean.price
        total_score += bean.intensity + bean.acidity

print("\nPodsumowanie:")
print(f"Waga: {total_weight}")
print(f"Cena: {total_price}")
print(f"Ocena sensoryczna: {total_score}")

if total_weight <= maxWeight and total_price <= maxBudget:
    print("✅ Mieszanka spełnia ograniczenia wagi i budżetu")
else:
    print("❌ Mieszanka przekracza ograniczenia")
