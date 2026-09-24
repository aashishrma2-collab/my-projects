events = []

def add_event():
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    venue = input("Enter venue: ")

    event = {
        "name": name,
        "date": date,
        "venue": venue
    }

    events.append(event)
    print("Event added successfully!")


def view_events():
    if not events:
        print("No events available.")
        return

    for event in events:
        print("\nEvent:", event["name"])
        print("Date:", event["date"])
        print("Venue:", event["venue"])


def search_event():
    name = input("Enter event name to search: ")

    for event in events:
        if event["name"].lower() == name.lower():
            print("\nEvent Found!")
            print("Event:", event["name"])
            print("Date:", event["date"])
            print("Venue:", event["venue"])
            return

    print("Event not found.")


while True:
    print("\n--- College Event Management System ---")
    print("1. Add Event")
    print("2. View Events")
    print("3. Search Event")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        search_event()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
