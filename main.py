import random

# Total seats
TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}

# Function to check availability
def check_availability():
    print("\nAvailable Seats:", len(available_seats))
    print("Seat Numbers:", available_seats)

# Function to book ticket
def book_ticket():
    if not available_seats:
        print("\nNo seats available!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    seat = available_seats.pop(0)  # Assign first available seat
    booking_id = random.randint(1000, 9999)

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat)

# Function to view ticket
def view_ticket():
    booking_id = int(input("Enter Booking ID: "))

    if booking_id in bookings:
        data = bookings[booking_id]
        print("\n--- Ticket Details ---")
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Seat:", data["seat"])
    else:
        print("Invalid Booking ID!")

# Function to cancel ticket
def cancel_ticket():
    booking_id = int(input("Enter Booking ID to cancel: "))

    if booking_id in bookings:
        seat = bookings[booking_id]["seat"]
        available_seats.append(seat)
        available_seats.sort()

        del bookings[booking_id]
        print("Ticket Cancelled Successfully!")
    else:
        print("Invalid Booking ID!")

# Main menu
while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        check_availability()
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        view_ticket()
    elif choice == '4':
        cancel_ticket()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice, try again!")
