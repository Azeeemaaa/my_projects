def show_menu():
    print("\n=== Phonebook Menu ===")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Exit")


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"✅ Contact {name} added.")


def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("❌ Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact {name} deleted.")
    else:
        print("❌ Contact not found.")


def show_all_contacts(contacts):
    if not contacts:
        print("📭 Phonebook is empty.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def main():
    contacts = {}

    while True:
        show_menu()
        choice = input("Choose an action (1–5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            show_all_contacts(contacts)
        elif choice == '5':
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid input. Please try again.")


if __name__ == "__main__":
    main()
