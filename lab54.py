def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def all_contact(args, contacts):
    listall = [f"Name: {name} - Tel : {contacts[name]}" for name in contacts]
    return "\n".join(listall)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Потрібен ПІБ!"
        except KeyError:
            return "Нема такого ПІБ!"
        except ValueError:
            return "Потрібен ПІБ та номер!"
    return inner

@input_error    
def phone_contact(args, contacts):
    name = args[0]
    return f"Name: {name} - Tel : {contacts[name]}"

@input_error 
def change_contact(args, contacts):
    if phone_contact(args, contacts) == "Нема такого ПІБ!":
        return "Нема такого контакту"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact change."

@input_error
def add_contact(args, contacts):
    if phone_contact(args, contacts) == "Нема такого ПІБ!":
        name, phone = args
        contacts[name] = phone
        return "Контакт додано"
    else:
        return "Такой контакт вже Є"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))  
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()