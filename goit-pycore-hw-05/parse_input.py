def input_error(func):
    def inner(*args, **kwargs):
        # TODO: Напиши тут блок try-except
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not faund"
        except ValueError:
            return "Number not exist"
        except IndexError:
            return "Index Error"
            
        # try: виконай func
        # except ValueError: поверни "Give me name and phone please."
        # except KeyError: ...
        # except IndexError: ...
        
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contact):
    if len(args) != 2:
        return "invalid format"
    name, phone = args
    contact[name] = phone
    return "contact added"

@input_error
def change_contact(args, contact):
    if len(args) != 2:
        return "invalid format"
    name, phone = args
    if name in contact:
        contact[name] = phone
        return "contact updatet"
    

@input_error
def show_phone(args, contact):
    if len(args) != 1:
        return "invalid format"
    name = args[0]
    if name in contact:
        return contact[name]

    
@input_error
def show_all(contact):
    result = ""
    if not contact:
        return "Empty"
    for name, phone in contact.items():
        result += f"{name}: {phone}\n"
    return result



def main():
    contacts = {}
    print(f"Welcome to the assistant bot!")
    while True:
        us_imput = input('Enter a command:')
        if not us_imput:
            continue
        try:
            cmd, args = parse_input(us_imput)
        except ValueError:
            continue
        if cmd in ["exit", "close"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
            continue


if __name__=="__main__":
    main()