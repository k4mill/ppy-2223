import random

if __name__ == '__main__':
    cities = ['Bydgoszcz', 'Warszawa', 'Gdańsk', 'Gdynia', 'Wrocław', 'Kraków', 'Olsztyn', 'Toruń', 'Poznań', 'Łódź', 'Lublin', 'Szczecin']
    toVisit = []

    for i in range(0, 10):
        n = random.randint(0, 10)
        while cities[n] in toVisit:
            n = random.randint(0, 10)

        toVisit.append(cities[n])

    print(f"{toVisit}")
