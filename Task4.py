contacts = {}

def add_contact(name, phone_number, email, address):
    if name not in contacts:
        contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print("Contact added successfully.")
    else:
        print("Contact with this name already exists.")

def view_contact_list():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print("Name:", name)
            print("Phone Number:", details['phone_number'])
            print("Email:", details['email'])
            print("Address:", details['address'])
            print("-" * 20)
    else:
        print("No contacts found.")

def search_contact(keyword):
    found = False
    for name, details in contacts.items():
        if keyword in name or keyword == details['phone_number']:
            print("Name:", name)
            print("Phone Number:", details['phone_number'])
            print("Email:", details['email'])
            print("Address:", details['address'])
            print("-" * 20)
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact(name, phone_number=None, email=None, address=None):
    if name in contacts:
        if phone_number:
            contacts[name]['phone_number'] = phone_number
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            search_contact(keyword)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number (leave empty to keep current): ")
            email = input("Enter new email (leave empty to keep current): ")
            address = input("Enter new address (leave empty to keep current): ")
            update_contact(name, phone_number, email, address)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
