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

## Dane wejściowe

Każdy z wierszy pliku zawierającego zbiór uczący zawiera 3-elementowy ciąg liczb oddzielonych przecinkami. Pierwsze 2 elementy tego ciągu to liczby rzeczywiste oznaczające wartości zmiennych opisujących. Trzeci element to liczba naturalna z zakresu 0-5 oznaczająca wartość zmiennej celu - kategorię do której należy dana obserwacja.

### Przykładowe dane

```
5.1,3.5,0
4.9,3,0
4.7,3.2,1
4.6,3.1,1
5,3.6,2
5.4,3.9,2
4.6,3.4,3
5,3.4,3
4.3,3,4
```

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
