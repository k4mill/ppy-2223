# Zad 3

answers = []
questions = {
    "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?": {
        "A": "oglądanie telewizji/filmów/seriali",
        "B": "czytanie książek/czasopism",
        "C": "słuchanie muzyki",
        "D": "spotkania z rodziną/przyjaciółmi",
        "E": "podróżowanie",
        "F": "uprawianie sportu"
    },
    "W jakich okolicznościach czytasz książki najczęściej?": {
        "A": "podczas podróży",
        "B": "w czasie wolnym (po pracy, na urlopie)",
        "C": "podczas pracy/nauki (to ich element)",
        "D": "w ogóle nie czytam"
    },
    "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?": {
        "A": "chęć poszerzenia wiedzy",
        "B": "czytanie mnie relaksuje/odpręża",
        "C": "fakt, że czytanie jest modne",
        "D": "czytanie to moje hobby",
        "E": "konieczność nauki w związku z wykonywaną pracą/studiami",
        "F": "odczuwam presję rodziny/środowiska, żeby czytać"
    },
    "Po książki w jakiej formie sięgasz najczęściej?": {
        "A": "papierowej (tradycyjnej)",
        "B": "e-booki (książki elektroniczne) na komputerze",
        "C": "e-booki na tablecie/telefonie",
        "D": "e-booki na specjalnym czytniku (np. Kindle)"
    },
    "Ile książek czytasz średnio w ciągu roku?": {
        "A": "0",
        "B": "żadnej w całości - jedynie fragmenty",
        "C": "1",
        "D": "2 lub 3",
        "E": "4-10",
        "F": "powyżej 10"
    },
    "Jak często średnio czytasz książki?": {
        "A": "codziennie",
        "B": "raz w tygodniu",
        "C": "raz w miesiącu",
        "D": "raz na kilka miesięcy",
        "E": "raz na pół roku",
        "F": "raz na rok",
        "G": "wcale"
    },
    "Po jakie gatunki książek sięgasz najczęściej?": {
        "A": "kryminały/thrillery",
        "B": "horrory",
        "C": "fantastykę",
        "D": "science fiction",
        "E": "przygodowe",
        "F": "romanse",
        "G": "naukowe",
        "H": "psychologiczne",
        "I": "historyczne"
    }
}

answers.append(input("Jak masz na imię i nazwisko?\n"))

for key in questions:
    print(f"\n{key}")
    for letter in questions[key]:
        print(f"{letter}. {questions[key][letter]}")

    answers.append(input("Podaj literę: ")[0])

for index, ans in enumerate(answers):
    if index == 0:
        print(f"Jak masz na imię i nazwisko?\n{answers[index]}\n")
        continue
    print(f"Pytanie {index}: {list(questions)[index - 1]}\nOdpowiedź: {list(questions.values())[index - 1][ans.upper()]}\n")