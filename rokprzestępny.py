"""
Program sprawdza czy podany rok jest przestępny
"""

# wprowadzenie danych wejściowych
rok = int(input('Podaj rok: '))

# obliczenia
# wyrażenie zwraca wartość logiczną
czy_przestepny = (rok % 400 == 0) or (rok % 100 != 0) and (rok % 4 == 0)

# wypisanie wyniku
print('Czy rok', rok, 'jest przestępny?', czy_przestepny)


def rok_przystepny(param):
    pass


def test_rok_ma_byc_przystepny():
    assert rok_przystepny(2020) == True

def test_rok_ma_byc_nieprzystepny():
    assert rok_przystepny(2022) == False
