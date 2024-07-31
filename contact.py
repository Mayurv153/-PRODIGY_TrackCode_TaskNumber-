contacts = {}

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        print("Contacts List:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

def update_contact():
    name = input("Enter the contact name to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        contacts[name] = phone
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
f