# Barista Knapsack

## Opis projektu
Celem projektu jest stworzenie optymalnej mieszanki kawy przy zmieniających się danych dotyczących dostępnych ziaren. Każde ziarno kawy posiada określone parametry: waga, cena, intensywność smaku i kwasowość. Zadaniem jest wybranie najlepszej mieszanki przy ograniczeniach wagi i budżetu.

Projekt pozwala również na szybkie dostosowanie mieszanki do zmian, takich jak:
- dodanie nowych ziaren do oferty,
- zmiana ceny istniejących ziaren,
- zmiana maksymalnego budżetu.

Dzięki temu nie trzeba przeliczać wszystkich możliwych kombinacji od nowa.

---

## Dane wejściowe

Każde ziarno kawy posiada:
- **Waga** (g),
- **Cena** (zł),
- **Intensywność smaku** (1–10),
- **Kwasowość** (1–10).

Ograniczenia mieszanki:
- **Maksymalna waga mieszanki** (np. 250 g),
- **Maksymalny budżet** (np. 40 zł).

Ocena sensoryczna mieszanki jest obliczana na podstawie parametrów ziaren (wzór do ustalenia).

---

## Problem

- Początkowo należy stworzyć mieszankę kawy maksymalizującą ocenę sensoryczną przy zachowaniu ograniczeń wagi i budżetu.
- Po wprowadzeniu zmian w danych (nowe ziarna, zmiana cen, zmiana budżetu) należy szybko zaktualizować optymalną mieszankę, minimalizując czas obliczeń.

---

## Algorytm

Projekt wykorzystuje **problem plecakowy (0/1)**:

1. **Początkowa selekcja mieszanki**  
   Generowanie najlepszej możliwej kombinacji ziaren przy zadanych ograniczeniach.

2. **Aktualizacja mieszanki przy zmianach danych**  
   - Dodanie nowego ziarna,  
   - Zmiana ceny istniejącego ziarna,  
   - Zmiana maksymalnego budżetu.

Algorytm jest zoptymalizowany do szybkiej aktualizacji wyników bez pełnego przeliczania wszystkich kombinacji.

---

## Autorzy
- **Valeriia Khylchenko**  
- **Yana Trotsenko**
