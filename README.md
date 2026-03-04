# Mieszanka kawy - Problem aktualizacyjny

## Opis

Celem projektu jest rozwiązanie problemu stworzenia **najlepszej mieszanki kawy** przy zmieniających się danych. Początkowo mamy zestaw ziaren kawy, które mają przypisane parametry: waga, cena, intensywność smaku i kwasowość. Z tego zestawu należy wybrać mieszankę kawy, przy zachowaniu ograniczeń masy mieszanki i budżetu.

Po początkowej konfiguracji, pojawiają się zmiany w dostępnych danych:
- Nowe ziarna kawy mogą zostać dodane do oferty,
- Ceny ziaren mogą się zmieniać,
- Maksymalny budżet może zostać zaktualizowany.

Projekt ten rozwiązuje problem **aktualizacji wyboru mieszanki kawy**, czyli jak efektywnie dostosować najlepszy wybór ziaren przy zmieniających się warunkach, bez konieczności ponownego liczenia wszystkiego od zera.

## Problem

1. Masz zestaw dostępnych ziaren kawy. Każde ziarno posiada następujące parametry:
    - Waga (g),
    - Cena (zł),
    - Intensywność smaku (1–10),
    - Kwasowość (1–10).
   
2. Posiadasz **ograniczenia**:
    - **Maksymalna waga mieszanki** (np. 250 g),
    - **Maksymalny budżet** (np. 40 zł).

3. **Ocena sensoryczna** mieszanki obliczana jest na podstawie wzoru:
    ```
    dopiszemy
    ```

4. **Początkowe zadanie**:
    - Musisz stworzyć najlepszą możliwą mieszankę kawy, przy zachowaniu ograniczeń masy i budżetu.

5. **Zmiany / Aktualizacje**:
    - **Dodanie nowego ziarna** (np. cena 8 zł, waga 50 g, intensywność 9, kwasowość 6),
    - **Zmiana ceny** ziaren w ofercie,
    - **Zmniejszenie budżetu**.

6. Twoim zadaniem jest **aktualizacja najlepszego wyboru ziaren** przy nowych danych, stosując odpowiedni algorytm, który minimalizuje czas obliczeń, nie licząc wszystkiego od nowa.

## Algorytm

Projekt używa **algorytmu plecakowego (0/1)** do rozwiązania problemu wyboru mieszanki kawy. Początkowo generujemy rozwiązanie, a następnie implementujemy **aktualizację wyników** przy zmieniających się danych.

Dodatkowo, w przypadku zmiany danych (np. nowego ziarna, zmiany ceny), zaimplementowane algorytmy są w stanie **szybko zaktualizować najlepszą mieszankę** bez konieczności pełnego przeliczenia wszystkich możliwych kombinacji.

##Autorzy
Valeriia Khylchenko
Yana Trotsenko
