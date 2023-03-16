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