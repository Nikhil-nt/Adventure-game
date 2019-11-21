import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, filled with \n"
                "grass and yellow wildflowers.")
    print_pause('Rumor is that a demon is somewhere around here,and has \n'
                'been terrifying the nearby village.')
    print_pause('The demon takes the form of a wicked faire or a dragon.')
    print_pause('In front of you is a house')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold a trusty(but not very effective)dagger')


def choice_input(choice):
    print_pause('Enter 1 to knock on the door of the house.\n'
                'Enter 2 to peer into the cave.')
    print_pause('What would you like to do?')
    while True:
        response = input('please enter 1 or2')
        if response == '1':
            return response
            break
        elif response == '2':
            return response
            break
        else:
            print_pause(choice)


def house():
    print_pause('You approach the door of the house.')
    print_pause('You are about to knock when the door \n'
                'opens and out steps a dragon')
    print_pause("Eep! This is the dragon's house!")
    print_pause('The dragon attacks you!')


def option_input(choice):
    while True:
        option = input(choice)
        if option == '1':
            return option
        elif option == '2':
            return option
        else:
            print_pause(choice)


def fight_defeat():
    print_pause('You can do your best')
    print_pause('But your dagger is no match for the wicked faire')
    print_pause('You have been defeated!')


def ask_input(ask):
    while True:
        choice = input('Would you like to play again? (y/n)\n')
        if choice == 'y':
            print_pause('Restarting the game!')
            play_game()
            break
        elif choice == 'n':
            print_pause('Thanks for playing!')
            break
        else:
            print(ask)


def field():
    print_pause("You run back into the field. Luckily, \n"
                "you don't seem to be followed.")


def cave():
    print_pause('You peer cautiously into the cave.')
    print_pause('It turns out to be a very small cave.')
    print_pause('Your eye catches a glint of metal behind a rock.')
    print_pause('You found a magical sword og Ogroth')
    print_pause('You discard your silly old weapon and take the word with you')


def faire_house():
    print_pause('You approach the door of the house')
    print_pause('You are about to knock when the door \n'
                'opens and steps out a wicked faire')
    print_pause("Eep! This is a wicked fairie's house!")
    print_pause("The wicked fairie attacks you!")


def reminder_cave():
    print_pause('You have been to this cave. There is nothing left!')


def fight_house():
    demons = ['dragon', 'wicked faire']
    demon = random.choice(demons)
    demon1 = demon
    if 'dragon' in demon1:
        print_pause('You take your sword and rush to kill the dragon.')
        print_pause('The dragon flies above you and blows fire.')
        print_pause('You dodge the fire and increase the size of the sword.')
        print_pause('The dragon smashes you with the tail and you fall down.')
        print_pause('You pretend to be dead, the dragon \n'
                    'moves slowly towards you.')
        print_pause('You pickup the sword and make an \n'
                    'attack and the dragon is dead.')
        print_pause('Congratulations! You are victorious.')
    elif 'wicked faire' in demon1:
        print_pause('As the wicked fairie moves to attack,\n'
                    'you unsheath your new weapon.')
        print_pause('The sword shines brightly in your hand as \n'
                    'you brace yourself for the attack.')
        print_pause('But the wicked fairie takes one look at \n'
                    'your shiny new toy and runs away!')
        print_pause('You have rid the town of the wicked \n'
                    'fairie. You are victorious!')


def game_begins():
    choice1 = choice_input("please enter 1 or 2")
    if choice1 == '1':
        house()
        option1 = option_input('Would you like to (1) fight or (2) run away')
        if option1 == '1':
            fight_defeat()
            ask_input('Would you like to play again? (y/n)\n')
        elif option1 == '2':
            field()
            game_begins()
    elif choice1 == '2':
        cave()
        field()
        while True:
            choice1 = choice_input("please enter 1 or 2")
            if choice1 == '1':
                faire_house()
                option1 = option_input('Would you like to (1) \n'
                                       'fight or (2) run away')
                if option1 == '1':
                    fight_house()
                    ask = ask_input('Would you like to play again? (y/n)\n')
                    break
                elif option1 == '2':
                    field()
            elif choice1 == '2':
                reminder_cave()
                field()


def play_game():
    intro()
    game_begins()


play_game()
