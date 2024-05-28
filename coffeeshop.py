def main():
    drinks = ('Chokolate', 'Coffee', 'Decaf')
    flavors = ('Caramel', 'Vanilia', 'Peppermint', 'Raspberry', 'Plain')
    toppings = ('Chokolate', 'Cinnamon', 'Caramel')

    drink = menu(drinks, "Erik`s drinks", 'Choose your drink: ')
    flavor = menu(flavors, "Erik's flavors", 'Choose your flavor:  ')
    topping = menu(toppings, "Erik's toppings", 'Choose yout flavors: ')

    print()
    print("Here is your order:")
    print(f'Main product - {drink}')
    print(f'Flavor - {flavor}')
    print(f'topping - {topping}')
    print("Thanks for your order!")


def menu(choices, title="Erik's menu", prompt="Choose your item: "):
    print()
    print(title)
    print(len(title) * '-')
    item = 1
    for choice in choices:
        print(f'{item} - {choice}')
        item += 1

    while True:
        user_choice = input(prompt)
        allowed_answers = []    
        for i in range(1, len(choices) + 1):
            allowed_answers.append(str(i))

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


if __name__ == '__main__':
    main()
