from hang_man_shapes import hang_man
import random as r


def user_name():
    name = input("Dear User Enter Your Name:").upper()
    return name


def start(name):
    print("###########################################################################")
    print("This Program Plays A Game of Hangman.")
    print(name+" Guess Letters In The Mystery Word.")
    print("Guess A Country.")
    print("You Can Only Make 8 Incorrect Guesses Before You Lose.")
    print("See If You Can Guess The Word Before You Run Out Of Guesses...")
    print("###########################################################################")


def word():
    countries = ["PAKISTAN", "INDIA", "AUSTRALIA", "ENGLAND", "WEST INDIES",
                 "NEW ZEALAND", "SRI LANKA", "AFGHANISTAN", "SOUTH AFRICA", "BANGLADESH"]
    random_word = r.choice(countries)
    return random_word


def store(random_list):
    store = []
    for i in range(len(random_list)):
        if random_list[i] == " ":
            store.append(" ")
        else:
            store.append("_")
    return store


def valid_check(user):
    valid = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    while True:
        if user in valid:
            break
        else:
            print("Please Enter A Valid Digit")
            user = input("\nEnter A Digit: ").upper()
    return user


def repeat_check(repeat, user):
    while True:
        if user in repeat:
            print("You Already Guessed That Letter")
            user = valid_check(input("\nEnter A Digit: ").upper())
        else:
            repeat.append(user)
            break
    return user


def comment(random_list, user, incorrect):
    if user in random_list:
        print("Good Guess... '"+user+"' is in the word")
    else:
        print("Sorry there is no '"+user+"' in the word")
        incorrect = incorrect-1
    return incorrect


def result(store_list, random_list, incorrect, name):
    if "".join(store_list) == "".join(random_list):
        print("Dear ", name, " Congratulations You Win")
        print("word: ", " ".join(random_list))
        return "done"
    elif incorrect == 0:
        print("Sorry ", name, " You Didn't Win This Time... Best of luck for next time")
        print("word: ", " ".join(random_list))
        return "done"
    else:
        print("word: ", " ".join(store_list))
        print("Incorrect Guesses Left: ", incorrect)


def play(name):
    incorrect = 8
    random_word = word()
    random_list = list(random_word)
    store_list = store(random_list)
    repeat = []
    print("\nword: ", " ".join(store_list))
    print("Incorrect Guesses Left: ", incorrect)
    while True:
        user = valid_check(input("\nEnter A Digit: ").upper())

        user = repeat_check(repeat, user)
        incorrect = comment(random_list, user, incorrect)
        hang_man(incorrect)

        for i in range(len(store_list)):
            if random_list[i] == user:
                store_list[i] = user
        final = result(store_list, random_list, incorrect, name)
        if final == "done":
            break
    play_again(name)


def play_again(name):
    condition = input(
        "Press 'y' or 'yes' to play again or any other key to end:").lower()
    while condition == "y" or condition == "yes":
        play(name)
        break


def main():
    name = user_name()
    start(name)
    play(name)


main()
