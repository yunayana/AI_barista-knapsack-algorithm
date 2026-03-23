import csv
import random
import sys

class CoffeeBean:
    def __init__(self, name, weight, price, intensity, acidity):
        self.name = name
        self.weight = float(weight)
        self.price = float(price)
        self.sensory_score = float(intensity) + float(acidity)

class BaristaKnapsackHS:
    def __init__(self, csv_path, max_weight, max_budget, hms=10, hmcr=0.7, par=0.3, mutation_rate=0.02):
        self.csv_path = csv_path
        self.max_weight = max_weight
        self.max_budget = max_budget
        self.hms = hms
        self.hmcr = hmcr 
        self.par = par
        self.mutation_rate = mutation_rate  #  MUTACJA
        self.beans = self.load_data()
        self.hm = []

    def load_data(self):
        beans = []
        try:
            with open(self.csv_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    beans.append(CoffeeBean(row['name'], row['weight'], row['price'], row['intensity'], row['acidity']))
            print(f"[SYSTEM] Wczytano {len(beans)} ziaren z bazy.")
            return beans
        except Exception as e:
            print(f"BŁĄD PLIKU: {e}")
            return []

    def calculate_fitness(self, sol):
        w, p, s = 0, 0, 0
        for i, selected in enumerate(sol):
            if selected:
                w += self.beans[i].weight
                p += self.beans[i].price
                s += self.beans[i].sensory_score
        if w > self.max_weight or p > self.max_budget or w == 0:
            return 0
        return s

    def solve(self, iterations=10000):
        if not self.beans: return None
        
        print(f"--- START (Waga: {self.max_weight}, Budżet: {self.max_budget}) ---")
        
        # licznik mutacji
        mutation_counter = 0
        
        # 1. INICJALIZACJA HM
        print("Inicjalizacja pamięci HM...")
        while len(self.hm) < self.hms:
            sol = [0] * len(self.beans)
            indices = list(range(len(self.beans)))
            random.shuffle(indices)
            
            curr_w, curr_p = 0, 0
            for idx in indices:
                if curr_w + self.beans[idx].weight <= self.max_weight and \
                   curr_p + self.beans[idx].price <= self.max_budget:
                    sol[idx] = 1
                    curr_w += self.beans[idx].weight
                    curr_p += self.beans[idx].price
                
            fit = self.calculate_fitness(sol)
            if fit > 0:
                self.hm.append({'sol': sol, 'fit': fit})

        print(f"[OK] Pamięć HM gotowa. Rozpoczynam improwizację...")

        # 2. GŁÓWNA PĘTLA
        for i in range(1, iterations + 1):
            new_sol = []
            
            for j in range(len(self.beans)):
                if random.random() < self.hmcr:
                    random_idx = random.randint(0, self.hms - 1)
                    val = self.hm[random_idx]['sol'][j]

                    if random.random() < self.par:
                        val = 1 - val

                    new_sol.append(val)
                else:
                    new_sol.append(1 if random.random() < 0.05 else 0)

            # 🔥 --- MUTACJA ---
            mutations_in_this_iter = 0
            for j in range(len(new_sol)):
                if random.random() < self.mutation_rate:
                    new_sol[j] = 1 - new_sol[j]
                    mutations_in_this_iter += 1

            mutation_counter += mutations_in_this_iter

            # ocena
            new_fit = self.calculate_fitness(new_sol)

            if new_fit > 0:
                self.hm.sort(key=lambda x: x['fit'])
                if new_fit > self.hm[0]['fit']:
                    self.hm[0] = {'sol': new_sol, 'fit': new_fit}
            
            # pasek postępu + mutacje
            if i % 50 == 0 or i == iterations:
                percent = int((i / iterations) * 100)
                sys.stdout.write(
                    f"\rOptymalizacja: {percent}% "
                    f"[{'#' * (percent // 5)}{'.' * (20 - percent // 5)}] "
                    f"Best Fit: {max(x['fit'] for x in self.hm):.1f} "
                    f"| Mutacje: {mutation_counter}"
                )
                sys.stdout.flush()

        print("\n--- ZAKOŃCZONO ---")

        best = max(self.hm, key=lambda x: x['fit'])
        best['mutations'] = mutation_counter  #  dodajemy do wyniku
        return best


if __name__ == "__main__":
    problem = BaristaKnapsackHS(
        "coffee_beans.csv",
        max_weight=250,
        max_budget=40,
        hms=10,
        hmcr=0.7,
        par=0.3,
        mutation_rate=0.02
    )

    wynik = problem.solve(10000)
    
    if wynik:
        print(f"\nSKŁAD MIESZANKI (Suma punktów: {wynik['fit']}):")
        w_t, p_t = 0, 0

        for i, s in enumerate(wynik['sol']):
            if s:
                b = problem.beans[i]
                w_t += b.weight
                p_t += b.price
                print(f" * {b.name:12} | {b.weight}g | {b.price}zł | Sens: {b.sensory_score}")

        print(f"\nPodsumowanie: Waga {w_t}/{problem.max_weight}g, Koszt {p_t}/{problem.max_budget}zł")
        print(f"Łączna liczba mutacji: {wynik['mutations']}")
