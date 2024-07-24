import json
import os

CONTACTS_FILE = 'contacts.json'


# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}


# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email address: ").strip()

    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")


# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ").strip()
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email address (leave blank to keep current): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        save_contacts(contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print(f"No contact found with the name {name}.")


# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}.")


# Main function
def main():
    contacts = load_contacts()

    while True:
        # Display menu
        print("\nContact Management System")
        print("=========================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Thank you for using the Contact Management System! :)")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
