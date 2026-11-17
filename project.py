import csv

class Flight:
    def __init__(self, no, origin, dest, seats, fare):
        self.no = no
        self.origin = origin
        self.dest = dest
        self.seats = seats
        self.fare = fare

    def book(self, n):
        self.seats -= n

    def cancel(self, n):
        self.seats += n

flights = []
try:
    for r in list(csv.reader(open("flights.csv")))[1:]:
        flights.append(Flight(r[0], r[1], r[2], int(r[3]), int(r[4])))
except FileNotFoundError:
    print("flights.csv file not found")

bookings = []

while True:
    print("\n1. Search flights\n2. Book\n3. Cancel booking\n4. Exit")
    c = input("Menu: ")

    if c == "1":
        o = input("Origin: ").lower()
        d = input("Destination: ").lower()
        res = [f for f in flights if f.origin.lower() == o and f.dest.lower() == d]
        for f in res:
            print(f.no, "|", f.origin, "->", f.dest, "| Seats:", f.seats, "| Fare: Rs.", f.fare, "per seat")
        if not res:
            print("No flights found")

    elif c == "2":
        no = input("Flight: ")
        name = input("Passenger: ")
        n = int(input("Seats: "))
        f = next((x for x in flights if x.no.lower() == no.lower()), None)
        if f == None:
            print("Flight", no, "not found")
        elif f.seats == 0:
            print("Flight", f.no, "is full.")
        elif n < 1:
            print("Number of seats must be at least 1.")
        elif n > f.seats:
            print("Only", f.seats, "seat(s) available on", f.no + ".")
        else:
            f.book(n)
            bid = "BK" + str(len(bookings) + 1)
            bookings.append([bid, f, n])
            print("Booking confirmed. ID:", bid, "|", name, "|", f.no, "|", n, "seat(s) | Total: Rs.", n * f.fare, "| Seats left:", f.seats)

    elif c == "3":
        bid = input("Booking ID: ")
        b = next((x for x in bookings if x[0].lower() == bid.lower()), None)
        if b == None:
            print("Booking", bid, "not found")
        else:
            b[1].cancel(b[2])
            bookings.remove(b)
            print("Booking", b[0], "cancelled. Seats left on", b[1].no + ":", b[1].seats)

    elif c == "4":
        print("Thank you")
        break

    else:
        print("Invalid choice")