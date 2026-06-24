# Task: Movie ticket booking with constructor validation

# Build a Ticket class whose constructor validates seat availability.

# Create a class Ticket with a constructor init (self, movie, seats_available, seats_requested) that calculates and stores self.confirmed_seats - the smaller of seats_available and seats_requested - plus a message attribute saying whether the full request was met. Create 3 Ticket objects with different availability scenarios and print each one's outcome.


class Ticket:
    def __init__(self, movie, seats_available, seats_requested):
        self.movie = movie
        self.confirmed_seats = min(seats_available, seats_requested)

        if seats_requested <= seats_available:
            self.message = "Full request confirmed."
        else:
            self.message = f"Only {self.confirmed_seats} seat(s) could be booked."


t1 = Ticket("Kalki", 100, 12)
t2 = Ticket("Kalki", 1, 12)
t3 = Ticket("Kalki", 100, 100)

tickets = [t1, t2, t3]

for ticket in tickets:
    print(f"\nMovie: {ticket.movie}")
    print(f"Confirmed Seats: {ticket.confirmed_seats}")
    print(f"Status: {ticket.message}")


























