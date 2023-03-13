import sys

# Zad 1

a = b = c = "Python 2023"
sys.getrefcount(a) # 4

print(a == b) # True
print(b == c) # True
print(type(a), type(b), type(c)) # <class 'str'> <class 'str'> <class 'str'>
print(hex(id(a)), hex(id(b)), hex(id(c))) # 0x1e637e7e5b0 0x1e637e7e5b0 0x1e637e7e5b0

print("\n-------------------\n")

c = "Java 11"
print(a == b) # True
print(b == c) # False
print(type(a), type(b), type(c)) # <class 'str'> <class 'str'> <class 'str'>
print(hex(id(a)), hex(id(b)), hex(id(c))) # 0x1e637e7e5b0 0x1e637e7e5b0 0x1e637e7e4f0

# Zad 2

try:
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    op = input("Podaj operator: ")
    res = 0

    match (op):
        case "+":
            res = a + b
        case "-":
            res = a - b
        case "*":
            res = a * b
        case "/":
            if (b != 0):
                res = a / b
            else:
                res = "błąd - dzielenie przez 0"
        case "**":
            res = a ** b
        case "//":
            res = a // b
        case "%":
            res = a % b
        case _:
            res = "błąd - zły operator"

    print("Wynik: " + str(res))

except ValueError:
    print("Zła wartość!")


# Zad 3

answers = []
questions = {
    "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?\n": {
        "A": "oglądanie telewizji/filmów/seriali",
        "B": "czytanie książek/czasopism",
        "C": "słuchanie muzyki",
        "D": "spotkania z rodziną/przyjaciółmi",
        "E": "podróżowanie",
        "F": "uprawianie sportu",
        "G": "inne, jakie?"
    },
    "W jakich okolicznościach czytasz książki najczęściej?\n": {
        "A": "podczas podróży",
        "B": "w czasie wolnym (po pracy, na urlopie)",
        "C": "podczas pracy/nauki (to ich element)",
        "D": "w ogóle nie czytam",
        "E": "inne, jakie?"
    },
    "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n": {
        "A": "chęć poszerzenia wiedzy",
        "B": "czytanie mnie relaksuje/odpręża",
        "C": "fakt, że czytanie jest modne",
        "D": "czytanie to moje hobby",
        "E": "konieczność nauki w związku z wykonywaną pracą/studiami",
        "F": "odczuwam presję rodziny/środowiska, żeby czytać",
        "G": "inny, jaki?"
    },
    "Po książki w jakiej formie sięgasz najczęściej?\n": {
        "A": "papierowej (tradycyjnej)",
        "B": "e-booki (książki elektroniczne) na komputerze",
        "C": "e-booki na tablecie/telefonie",
        "D": "e-booki na specjalnym czytniku (np. Kindle)"
    },
    "Ile książek czytasz średnio w ciągu roku?\n": {
        "A": "0",
        "B": "żadnej w całości - jedynie fragmenty",
        "C": "1",
        "D": "2 lub 3",
        "E": "4-10",
        "F": "powyżej 10"
    },
    "Jak często średnio czytasz książki?\n": {
        "A": "codziennie",
        "B": "raz w tygodniu",
        "C": "raz w miesiącu",
        "D": "raz na kilka miesięcy",
        "E": "raz na pół roku",
        "F": "raz na rok",
        "G": "wcale"
    },
    "Po jakie gatunki książek sięgasz najczęściej?\n": {
        "A": "kryminały/thrillery",
        "B": "horrory",
        "C": "fantastykę",
        "D": "science fiction",
        "E": "przygodowe",
        "F": "romanse",
        "G": "naukowe",
        "H": "psychologiczne",
        "I": "historyczne",
        "J": "inne, jakie?"
    }
}

answers.append(input("Jak masz na imię i nazwisko?\n"))

for key in questions:
    print(f"{questions[key]}\n")
    for letter in questions[key]:
        print(f"{letter}. {questions[key[letter]]}\n")

    answers.append(input("Podaj literę: "))

for index, ans in enumerate(answers):
    print(f"Pytanie {index + 1}: {questions[index]}Odpowiedź: {ans}\n")