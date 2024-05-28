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

    user_choice = input(prompt)
    answer = choices[int(user_choice) - 1]

    return answer




if __name__ == '__main__':
    main()
