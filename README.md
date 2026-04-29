# Barista Knapsack
https://aibarista-knapsack-algorithm-ilnfgkjahsqcyagdjtgwn2.streamlit.app
## Opis projektu
Celem projektu jest stworzenie optymalnej mieszanki kawy przy zmieniających się danych dotyczących dostępnych ziaren. Każde ziarno kawy posiada parametry: waga, cena, intensywność smaku i kwasowość. Zadaniem jest wybranie mieszanki maksymalizującej ocenę sensoryczną przy ograniczeniach wagi i budżetu.

Projekt pozwala także na szybkie dostosowanie mieszanki do zmian, takich jak:
- dodanie nowych ziaren do oferty,
- zmiana ceny istniejących ziaren,
- zmiana maksymalnego budżetu.

Dzięki temu nie trzeba przeliczać wszystkich możliwych kombinacji od nowa.

---

## Dane wejściowe

Każde ziarno kawy posiada:
- **Waga** (g)
- **Cena** (zł)
- **Intensywność smaku** (1–10)
- **Kwasowość** (1–10)

Ograniczenia mieszanki:
- **Maksymalna waga mieszanki** (np. 250 g)
- **Maksymalny budżet** (np. 40 zł)

Ocena sensoryczna mieszanki jest obliczana na podstawie parametrów ziaren (wzór do ustalenia).

---

## Problem

Projekt rozwiązuje **problem plecakowy 0/1**, czyli wybór podzbioru ziaren kawy maksymalizujący ocenę sensoryczną przy zachowaniu ograniczeń wagi i budżetu.

Zadania do wykonania:
1. Stworzenie początkowej mieszanki optymalnej.  
2. Aktualizacja mieszanki przy zmianach danych (nowe ziarna, zmiana cen, zmiana budżetu) w sposób szybki i efektywny.

---

## Rozwiązanie

1. **Początkowa selekcja mieszanki**  
   Generowanie najlepszego możliwego zestawu ziaren przy zadanych ograniczeniach.

2. **Aktualizacja mieszanki przy zmianach danych**  
   - Dodanie nowego ziarna  
   - Zmiana ceny istniejącego ziarna  
   - Zmiana maksymalnego budżetu  

Algorytm dynamiczny pozwala szybko przeliczyć najlepszą mieszankę bez pełnego przeszukiwania wszystkich kombinacji.

---

## Autorzy
- Valeriia Khylchenko  
- Yana Trotsenko
