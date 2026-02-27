contacts = []
def add_a_contact():
    name = input("Enter your name:")
    phone_no = input("Enter your phone no:")
    contacts.append({"name": name, "phone_no": phone_no})
    print("Contact added!")

def view_contact():
    if len(contacts) == 0:
        print("No contacts yet.")
    else:
        for c in contacts:
            print("name:", c["name"], "phone_no:", c["phone_no"])
def main():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Quit")
        choice = input("Enter your choice:")
        if choice == "1":
            add_a_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
main()