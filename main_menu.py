def main_menu():
    while True:
        order = get_order()
        print('Check your order: ')
        print_order(order)
        confirm = input('Confirm? Press Y yo confirm, N to cancel: ')

        if confirm.lower() == 'y':
            save_order(order)
            print()
            print('Thanks for your order: ')
            print()
            print_order(order)
        else:
            continue


def menu(choices, title="Erik's menu", prompt="Choose your item: "):
    # User dialogue function
    print()
    print(title)
    print(len(title) * '-')
    
    # Output dashes in the number of letters
    item = 1
    for choice in choices:
        print(f'{item} - {choice}')
        item += 1

    # Controling user input
    while True:
        user_choice = input(prompt)
        allowed_answers = []
        for i in range(1, len(choices) + 1):
            allowed_answers.append(str(i))

        # Adding the ability to skip question
        allowed_answers.append('X')
        allowed_answers.append('x')

        if user_choice in allowed_answers:
            if user_choice == 'X' or user_choice == 'x':
                answer = ''
                break
            else:
                answer = choices[int(user_choice) - 1]
            break
        else:
            print(f'Enter number from 1 to {len(choices)}')
            answer = ''

    return answer


def read_menu(filename):
    # The function of reading from a file
    my_file = open(filename, 'r', encoding='utf-8')
    resoult = my_file.readlines()
    for item in range(len(resoult)):
        resoult[item] = resoult[item].rstrip('\n')
    my_file.close
    
    return resoult


def get_order():
    """The function of receiving an order and filling the dictionary
    with it"""
    order = {}

    drinks = read_menu("drinks.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")

    order['name'] = input("What's your name: ")
    order['drink'] = menu(drinks, "Erik's drinks", "Choose your drink: ")
    order['flavor'] = menu(flavors, "Erik's flavors", "Choose your flavors: ")
    order['topping'] = menu(toppings, "Eriks toppings",
                            "Choose your topping: ")

    return order


def print_order(order):
    """The print of order"""
    print()
    print(f"Here is your order: {order['name']}")
    print(f"Main product: {order['drink']}")
    print(f"Flavor: {order['flavor']}")
    print(f"Topping: {order['topping']}")
    print("Thanks for your order!")
    print()

    return


def save_order(order):
    print('Saving order..')
    return


if __name__ == "__main__":
    main_menu()
