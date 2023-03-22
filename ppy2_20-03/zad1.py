if __name__ == '__main__':
    numbers = input("Podaj liczby rozdzielone przecinkami: ")
    numbers = numbers.split(",")
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

        if number < min:
            min = number

    print(f"max: {max}\nmin: {min}")



