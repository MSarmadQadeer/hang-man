from hang_man_shapes import hang_man
import random as r
name = input("Dear User Enter Your Name:").upper()
print("###########################################################################")
print("This Program Plays A Game of Hangman.")
print(name+" Guess Letters In The Mystery Word.")
print("Guess A Country.")
print("You Can Only Make 8 Incorrect Guesses Before You Lose.")
print("See If You Can Guess The Word Before You Run Out Of Guesses...")
print("###########################################################################")

condition = "y"
while condition == "y" or condition == "yes":
    countries = ["PAKISTAN", "INDIA", "AUSTRALIA", "ENGLAND", "WEST INDIES",
                 "NEW ZEALAND", "SRI LANKA", "AFGHANISTAN", "SOUTH AFRICA", "BANGLADESH"]
    random_word = r.choice(countries)
    random_list = list(random_word)
    valid = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    check = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    store = []
    incorrect = 8

    for i in range(len(random_list)):
        if random_list[i] == " ":
            store.append(" ")
        else:
            store.append("_")

    print("\nword: ", " ".join(store))
    print("Incorrect Guesses Left: ", incorrect)

    while incorrect > 0:
        user = input("\nEnter A Digit: ").upper()
        if user in valid:
            if user in check:
                if user in random_list:
                    print("Good Guess... '"+user+"' is in the word")
                else:
                    print("Sorry there is no '"+user+"' in the word")
                    incorrect = incorrect-1
                for k in range(len(check)):
                    if check[k] == user:
                        check[k] = "-"
            else:
                print("You Already Guessed That Letter")
                continue
        else:
            print("Please Enter A Valid Digit")
            continue

        hang_man(incorrect)

        for j in range(len(random_list)):
            if user == random_list[j]:
                store[j] = user

        if "".join(store) == "".join(random_list):
            print("Dear ", name, " Congratulations You Win")
            print("word: ", " ".join(random_list))
            break

        if incorrect == 0:
            print("Sorry ", name,
                  " You Didn't Win This Time... Best of luck for next time")
            print("word: ", " ".join(random_list))
            break

        print("word: ", " ".join(store))
        print("Incorrect Guesses Left: ", incorrect)

    condition = input(
        "Press 'y' or 'yes' to play again or any other key to end:").lower()
