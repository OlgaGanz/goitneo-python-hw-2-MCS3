def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Wrong number of parameters."
        except Exception as e:
            return f"Unknown error: {e}"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone for {name} changed."
    else:
        return f"User {name} not found."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts.get(name, f"No phone for {name} found.")

def show_all_contacts(contacts):
    return '\n'.join([f"{username}: {phone}" for username, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
