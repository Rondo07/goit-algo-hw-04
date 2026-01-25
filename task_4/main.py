

def parse_input(user_input):
    cmd, *args = user_input.split()   # Split user input into command and arguments
    cmd = cmd.strip().lower()   # Remove spaces, make lowercase
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args   # Unpack name and phone from arguments
    contacts[name] = phone   # Save contact to dict
    return "Contact added."

def show_phone(args, contacts):
    name = args[0]   # Get contact name from arguments
    if name in contacts:   # Check if contact exists
        return contacts[name]
    else:
        return "Contact not found"
    
def show_all(contacts):
    contact_list = []   # Create list to store contacts
    for name, phone in contacts.items():   # Iterate over all contacts in dict
        contact_list.append(f"{name}: {phone}")   # Add contact to list
    return contact_list

def change_contact(args, contacts):
    name, phone = args   # Unpack name and new phone number
    if name in contacts:   # Update phone if contact exists
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Contact not found"

def main():
    contacts = {}   # Create dict to store contacts
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)   # Parse command and arguments

        if command in ["close", "exit"]:  # Command to exit
            print("Good bye!")
            break
        elif command == "hello":   # Greeting command
            print("How can I help you?")
        elif command == "add":   # Command to add contact
            print(add_contact(args, contacts))
        elif command == "phone":   # Command to show phone
            print(show_phone(args, contacts))
        elif command == "all":   # Command to show all contacts
            contact_list = show_all(contacts)
            if not contact_list:
                print("No contacts")
            else:
                print("\n".join(contact_list))
        elif command == "change":   # Command to change phone
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
