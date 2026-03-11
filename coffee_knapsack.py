import random


maxWeight = 250
maxBudget = 40



class CoffeeBean:

    def __init__(self, weight, price, intensity, acidity):
        self.weight = weight
        self.price = price
        self.intensity = intensity
        self.acidity = acidity



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
    CoffeeBean(55, 9, 8, 5),
    CoffeeBean(25, 3, 4, 2),
    CoffeeBean(65, 12, 9, 6),
    CoffeeBean(90, 14, 10, 7),
    CoffeeBean(15, 2, 2, 3),
    CoffeeBean(100, 15, 10, 9),
    CoffeeBean(10, 1, 1, 1),
    CoffeeBean(85, 13, 9, 8),
    CoffeeBean(75, 12, 8, 6),
    CoffeeBean(95, 14, 10, 7),
    CoffeeBean(30, 4, 5, 4),
    CoffeeBean(40, 6, 6, 5),
    CoffeeBean(55, 8, 7, 6),
    CoffeeBean(60, 9, 8, 7),
    CoffeeBean(20, 3, 3, 2),
    CoffeeBean(45, 7, 6, 5),
    CoffeeBean(35, 5, 5, 4),
    CoffeeBean(50, 8, 7, 5),
    CoffeeBean(70, 11, 9, 7),
    CoffeeBean(80, 12, 10, 8),
    CoffeeBean(28, 4, 5, 3),
    CoffeeBean(22, 3, 4, 2),
    CoffeeBean(48, 7, 6, 5),
    CoffeeBean(52, 8, 7, 6),
    CoffeeBean(66, 10, 8, 7),
    CoffeeBean(77, 11, 9, 6),
    CoffeeBean(33, 5, 6, 5),
    CoffeeBean(44, 6, 6, 6),
    CoffeeBean(58, 9, 8, 5),
    CoffeeBean(62, 10, 9, 6),
    CoffeeBean(72, 11, 9, 7),
    CoffeeBean(18, 2, 3, 3),
    CoffeeBean(24, 3, 4, 4),
    CoffeeBean(26, 3, 4, 2),
    CoffeeBean(38, 5, 5, 4),
    CoffeeBean(42, 6, 6, 5),
    CoffeeBean(49, 7, 6, 6),
    CoffeeBean(53, 8, 7, 5),
    CoffeeBean(59, 9, 8, 6),
    CoffeeBean(63, 10, 9, 7),
    CoffeeBean(68, 11, 9, 6),
    CoffeeBean(74, 12, 10, 8),
    CoffeeBean(82, 13, 10, 9),
    CoffeeBean(92, 14, 10, 8),
    CoffeeBean(96, 15, 10, 9),
    CoffeeBean(12, 2, 2, 1),
    CoffeeBean(14, 2, 3, 2),
    CoffeeBean(16, 2, 3, 3),
    CoffeeBean(17, 3, 4, 2),
    CoffeeBean(21, 3, 4, 3),
    CoffeeBean(23, 3, 5, 3),
    CoffeeBean(27, 4, 5, 4),
    CoffeeBean(29, 4, 5, 3),
    CoffeeBean(31, 5, 6, 4),
    CoffeeBean(32, 5, 6, 5),
    CoffeeBean(34, 5, 6, 4),
    CoffeeBean(36, 6, 6, 5),
    CoffeeBean(37, 6, 7, 5),
    CoffeeBean(39, 6, 7, 4),
    CoffeeBean(41, 7, 7, 5),
    CoffeeBean(43, 7, 7, 6),
    CoffeeBean(46, 7, 7, 5),
    CoffeeBean(47, 8, 8, 6),
    CoffeeBean(51, 8, 8, 6),
    CoffeeBean(54, 8, 8, 7),
    CoffeeBean(56, 9, 8, 6),
    CoffeeBean(57, 9, 9, 7),
    CoffeeBean(61, 10, 9, 6),
    CoffeeBean(64, 10, 9, 7),
    CoffeeBean(69, 11, 9, 7),
    CoffeeBean(71, 11, 9, 8),
    CoffeeBean(73, 12, 10, 8),
    CoffeeBean(76, 12, 10, 7),
    CoffeeBean(78, 12, 10, 8),
    CoffeeBean(79, 13, 10, 9),
    CoffeeBean(81, 13, 9, 8),
    CoffeeBean(83, 13, 10, 9),
    CoffeeBean(84, 13, 9, 7),
    CoffeeBean(86, 14, 10, 8),
    CoffeeBean(87, 14, 10, 9),
    CoffeeBean(88, 14, 9, 8),
    CoffeeBean(89, 14, 10, 9),
    CoffeeBean(91, 15, 10, 8),
    CoffeeBean(93, 15, 10, 9),
    CoffeeBean(94, 15, 10, 9),
    CoffeeBean(97, 15, 10, 10),
    CoffeeBean(98, 15, 10, 9),
    CoffeeBean(99, 15, 10, 10),
    CoffeeBean(11, 2, 2, 2),
    CoffeeBean(13, 2, 3, 2),
    CoffeeBean(19, 3, 4, 3)
]



def print_beans():
    print("\nDostępne ziarna kawy:\n")
    for i, bean in enumerate(beans):
        print(
            "ID:", i,
            "| Waga:", bean.weight,
            "| Cena:", bean.price,
            "| Intensywność:", bean.intensity,
            "| Kwasowość:", bean.acidity
        )



def generate_solution():
    solution = [0] * len(beans)
    total_weight = 0
    total_price = 0
    indexes = list(range(len(beans)))
    random.shuffle(indexes)

    for i in indexes:
        bean = beans[i]
        if (total_weight + bean.weight <= maxWeight and
            total_price + bean.price <= maxBudget):
            solution[i] = 1
            total_weight += bean.weight
            total_price += bean.price

    return solution



def evaluate(solution):
    total_weight = 0
    total_price = 0
    score = 0

    print("\nWybrane ziarna:\n")

    for i in range(len(solution)):
        if solution[i] == 1:
            bean = beans[i]
            print("Ziarno", i)
            total_weight += bean.weight
            total_price += bean.price
            score += bean.intensity + bean.acidity

    print("\nPodsumowanie:")
    print("Waga:", total_weight)
    print("Cena:", total_price)
    print("Ocena sensoryczna:", score)

   
    if total_weight <= maxWeight and total_price <= maxBudget:
        print(" Mieszanka spełnia ograniczenia wagi i budżetu")
    else:
        print(" Mieszanka przekracza ograniczenia wagi lub budżetu")



print_beans()
solution = generate_solution()
print("\nRozwiązanie:", solution)
evaluate(solution)