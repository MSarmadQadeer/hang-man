import json
from hang_man_shapes import hang_man
import random as r


def yes_no_check(x):
    while True:
        yes_no_check_list = ["y", "yes", "no", "n"]
        if x in yes_no_check_list:
            return x
        else:
            x = input("Invalid Entry. Kindly Reply in 'yes' or 'no': ")


again = "y"
while again == "y" or again == "yes":
    name = input("Dear User Enter Your Name:").upper()
    print("###########################################################################")
    print("This Program Plays A Game of Hangman.")
    print(name+" Guess Letters In The Mystery Word.")
    print("You Can Only Make 8 Incorrect Guesses Before You Lose.")
    print("See If You Can Guess The Word Before You Run Out Of Guesses...")
    print("###########################################################################")
    win = 0
    score = 0
    play = 0

    def space(x):
        for i in range(x, 26):
            print(" ", end="")

    condition = "y"
    while condition == "y" or condition == "yes":
        print("\nPress 1 for Easy Mode\nPress 2 for Medium Mode\nPress 3 for Hard Mode")

        while True:
            x = input("Enter Choice: ")
            choice = ["1", "2", "3"]
            if x in choice:
                break
            else:
                x = input("Kindly Enter A Valid Choice: ")
        if x == "1":
            with open("data.json") as jsonFile:
                List = json.load(jsonFile)["easy"]
                jsonFile.close()
        if x == "2":
            with open("data.json") as jsonFile:
                List = json.load(jsonFile)["medium"]
                jsonFile.close()
        if x == "3":
            with open("data.json") as jsonFile:
                List = json.load(jsonFile)["hard"]
                jsonFile.close()
        random_word = r.choice(List)
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
                score = score+10
                play = play+1
                win = win+1
                print("Dear ", name, " Congratulations You Win")
                print("word: ", " ".join(random_list))
                break
            if incorrect == 0:
                play = play+1
                print("Sorry ", name,
                      " You Didn't Win This Time... Best of luck for next time")
                print("word: ", " ".join(random_list))
                break
            print("word: ", " ".join(store))
            print("Incorrect Guesses Left: ", incorrect)

        condition = input(
            "Press 'y' or 'yes' to play again or any other key to end:").lower()
    print("Dear ", name, " you Played:", play, " times and win:",
          win, " time and your score is:", score)

    # get data file
    with open("data.json") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()

    # add data new
    data["record"].append({
        "name": name,
        "score": score
    })

    # save data new
    with open("data.json", "w+") as jsonFile:
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()

    record = sorted(data["record"], key=lambda i: i["score"], reverse=True)

    print("\nLIST OF HIGH SCORES :\n")
    print("Player", end="")
    space(len("player"))
    print("|", "Score")
    print("------------------------------------")  # 36
    if len(record) >= 3:
        for k in range(0, 3):
            print(record[k]["name"], end="")
            space(len(record[k]["name"]))
            print("|", record[k]["score"])
    else:
        for k in range(len(record)):
            print(record[k]["name"], end="")
            space(len(record[k]["name"]))
            print("|", record[k]["score"])
    again = yes_no_check(input("\nDo you want to Run the code again: "))
