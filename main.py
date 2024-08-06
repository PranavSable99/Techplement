import json
import os

CONTACTS_FILE = 'contacts_simple.json'


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    if any(contact['name'].lower() == name.lower() for contact in contacts):
        print("Error: Contact name already exist.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")


def search_contact(contacts):
    name = input("Enter contact: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("No contact found.")


def update_contact(contacts):
    name = input("Enter name: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Current Phone: {contact['phone']}")
            print(f"Current Email: {contact['email']}")

            phone = input("Enter new phone number (leave empty to keep current): ").strip()
            email = input("Enter new email (leave empty to keep current): ").strip()

            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email

            save_contacts(contacts)
            print(f"Contact '{name}' updated.")
            return

    print("Contact not found.")


def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Exit")


def main():
    contacts = load_contacts()

    while True:
        display_menu()
        option = input("Enter option (1-4): ").strip()

        if option == '1':
            add_contact(contacts)
        elif option == '2':
            search_contact(contacts)
        elif option == '3':
            update_contact(contacts)
        elif option == '4':
            print("Exiting the contact management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
