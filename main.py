from requests import get
from json import loads
from terminaltables import AsciiTable

cities = ['Kraków', 'Suwałki', 'Szczecin', 'Wrocław']

def main():
    url ='https://danepubliczne.imgw.pl/api/data/synop/'
    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]

    for row in loads(response.text):
        if row['stacja'] in cities:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])

    table = AsciiTable(rows)
    print(table.table)

if __name__ == '__main__':
    print('Pogoda w czterech rejonach Polski:')
    main()
    