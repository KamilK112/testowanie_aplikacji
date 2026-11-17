
def oblicz_srednia(liczby):
    if len(liczby) == 0:
        raise ValueError("Podaj liczby bro")

    return sum(liczby) / len(liczby)


def main():
    print("Kalkulator średniej")

    try:
        dane = input("Podaj liczby: ")
        liczby = [float(x) for x in dane.split()]

        srednia = oblicz_srednia(liczby)

        print("Średnia wynosi:", srednia)

    except ValueError:
        print("spróbuj ponownie")


if __name__ == "__main__":
    main()
