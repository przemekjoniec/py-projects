def bookTickets(band, tickets, /, *, ticketType="standard", section="general"):
    print("Rezerwacja biletów: ")
    print("Zespół:", band)
    print("L. biletów:", tickets)
    print("Rodzaj biletów:", ticketType)
    print("Sekcja:", section)

band = input("Podaj nazwe zespołu: ")
tickets = int(input("Podaj liczbe biletów: "))

bookTickets(band, tickets)
