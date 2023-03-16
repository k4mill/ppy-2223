import webbrowser, requests

from playsound import playsound

if __name__ == '__main__':
    # Zad 3
    playsound('test.mp3')

    # Zad 4
    # przyklad działania:
    # #pageurl – pobrana strona, date-data w formacie rok miesiac dzien np. 20230126
    # #zapytanie do api:#http://archive.org/wayback/available?url=example.com&timestamp=20060101
    pageurl = input("Podaj strone internetowa: ")
    date = int(input("Podaj date [RRRRMMDD]: "))

    for i in range(0, 3):
        url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date - i)
        response = requests.get(url)
        d = response.json()
        page = d["archived_snapshots"]["closest"]["url"]
        webbrowser.open(page)