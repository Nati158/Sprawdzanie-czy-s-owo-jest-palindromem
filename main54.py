def czy_palindrom(slowo):
    return slowo == slowo[::-1]

slowo = "kajak"
if czy_palindrom(slowo):
    print(slowo, "jest palindromem.")
else:
    print(slowo, "nie jest palindromem.")
