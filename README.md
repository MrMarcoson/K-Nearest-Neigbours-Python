# Algorytm k-najbliższych sąsiadów

Autor: Marek Kasprowicz

![obraz](https://user-images.githubusercontent.com/67783947/206601131-863f46e6-c49d-4b45-928c-6983451fb42c.png)

## Zależności

- python
- pip
- PySimpleGUI
    >pip install pysimplegui
- Matplotlib
    >pip install matplotlib
- numpy
    >pip install numpy
  
## Uruchamianie programu
>python main.py

## Używanie programu

1. Wybierz plik z danymi:
   1. Kliknij "Browse" i zaznacz plik
   2. Scieżka do niego wyświetli się w okienku po lewej
2. Wybierz liczbę sąsiadów z zakresu 1-20
3. Wybierz sposób określania odległości - euklidesowa lub miejska
4. Wybierz sposób wyboru głosowania - prosty lub ważony
5. Kliknij przycisk "Submit"
6. Naciśnij w dowolne miejsca na grafie lewym przyciskiem myszy
    1. W naciśniętym miejscu pojawi się kwadrat pokolorowany na kolor klasy wyznaczonej przez algorytm k-nn
    2. Pod grafem wypisana zostanie klasa do której należy dany punkt
    3. Pod klasą zostaną wypisani najbliżsi sąsiedzi i informacje z nimi związane

## Kolory klas

Wedle sprecyzowanych danych wejściowych mogą istnieć klasy z przedziału 0-5.

| Klasa | Kolor   |
|-------|---------|
| 0     | magenta |
| 1     | cyan    |
| 2     | green   |
| 3     | yellow  |
| 4     | red     |
| 5     | blue    |


## Informacje zawarte w tabelce sąsiadów

| Zmienna | Opis                                                          |
|---------|---------------------------------------------------------------|
| x1      | Pierwsza zmienna w pliku wejściowym, odwzierciedlona na osi x |
| x2      | Druga zmienna w pliku wejściowym, odwzierciedlona na osi y    |
| y       | Klasa punktu                                                  |
| dist    | Odległość punktu od miejsca zaznaczonego                      |

*Ilość sąsiadów nie zawsze musi wynosić zaznaczoną liczbę z zakresu 1-20. Gdy istnieją sąsiedzi o tej samej odległości to wszystkie są brane pod uwagę. 