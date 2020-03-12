import time
import random


def print_pause(strings):
    print(strings)
    time.sleep(2)


def random_evil():
    evil = ["Dragon", "Pirate", "Wicked fairie", "troll"]
    randchar = random.choice(evil)

    return randchar


def intro(randchar):
    print_pause("You find yourself standing in an open filed,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumer has it that a {randchar} is somewhere around here,"
                " and has been terifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def restart_input():
    while True:
        restart = input("would you like to play again? (y/n)")
        if restart == "y" or restart == "n":
            break
        else:
            continue
    return restart


def fight():
    while True:
        fight_choice = input("Would you like to (1) fight or (2) run away?\n")
        if fight_choice == "1" or fight_choice == "2":
            break
        else:
            continue
    return fight_choice


def player_choice_func():
    while True:
        player_choice = input("(Please enter 1 or 2.)\n")
        if player_choice == "1" or player_choice == "2":
            break
        else:
            continue
    return player_choice


def house(items, randchar):
    if "magical sword of ogoroth" not in items:
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door"
                    f" opens and out steps a {randchar}")
        print_pause(f"Eep! This is the {randchar}\'s house!")
        print_pause(f"the {randchar} attacks you!")
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
        fight_choice = fight()
        if fight_choice == "1":
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {randchar}.")
            print_pause("You have been defeated!")
            restart_game()
        elif fight_choice == '2':
            print_pause("You run into the filed. Luckily, you don\'t seem to "
                        "have been followed.")
            field(items, randchar)
    elif "magical sword of ogoroth" in items:
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door opens "
                    f"and out steps a {randchar}")
        print_pause(f"Eep! This is the {randchar}\'s house!")
        print_pause(f"the {randchar} attacks you!")
        fight_choice = fight()
        if fight_choice == "1":
            print_pause(f"As the {randchar} attacks, you unsheath your sword.")
            print_pause("The sword of ogoroth shines brightly in your hand as "
                        "you brace yourself for the attack.")
            print_pause(f"But the {randchar} takes one look at your "
                        "shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {randchar}."
                        " You are victorious!")
            restart_game()
        elif fight_choice == '2':
            print_pause("You run into the filed. Luckily,"
                        " you don\'t seem to have been followed.")
            field(items, randchar)


def cave(items, randchar):
    if "magical sword of ogoroth" not in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical sword of ogoroth!")
        print_pause("You discard your silly old"
                    " dagger and take the sword with you.")
        print_pause("You walk back to the field.")
        items.append("magical sword of ogoroth")
        field(items, randchar)
    elif "magical sword of ogoroth" in items:
        print_pause("You peer caustiously into the cave")
        print_pause("You\'ve been here before,"
                    " and gotten all the good stuff."
                    " It\'s just an empty cave now.")
        print_pause("You walk back to the field.")
        field(items, randchar)


def field(items, randchar):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    player_choice = player_choice_func()
    if player_choice == "1":
        house(items, randchar)
    elif player_choice == "2":
        cave(items, randchar)


def restart_game():
    restart = restart_input()
    if restart == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif restart == "n":
        print_pause("Thanks for playing! See you next time.")
        exit()


def game_setup(items, randchar):
    intro(randchar)
    field(items, randchar)


def play_game():
    items = []
    randchar = random_evil()
    game_setup(items, randchar)


play_game()
