import json
from difflib import get_close_matches
# return the closest matches to the target string
import os

data = json.load(open("words_data.json"))


def meaning_of_word(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yes_or_no = "Did you mean %s instead? Enter Y if yes or N if no" % get_close_matches(
            word, data.keys())[0]

        if yes_or_no == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_or_no == "N":
            return "The Word Desn't Exist"
        else:
            return "Cannot Understand Your Entry"

    else:
        return "The Word Desn't Exist"


if __name__ == "__main__":
    os.system('clear')
    print("Find the meaning of the Word!\n")
    while True:

        word = input("Enter Word: ")
        print(f"\n")

        for item in meaning_of_word(word):
            print(f"  " + item)

        print(f"\n")
