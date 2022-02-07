#MadLib.py
#Name: Michael Latta
#Date: 2022-01-30
#Assignment: Lab 1

def main():
    #Ask user for words
    
    noun1 = input("Please type a noun: ")
    noun2 = input("Please type another noun: ")
    verb1 = input("Please type a verb: ")
    verb2 = input("Please type another verb: ")
    adjective1 = input("Please type a adjective: ")
    adjective2 = input("Please type another adjective: ")

    #Print the story with the user supplied words.

    print("There once was a " + noun1 + " named " + noun2)
    print(noun2 + " would " + verb1 + " and " + verb2 + " all day long.")
    print(noun2 + " had hair that was " + adjective1 + " and " + adjective2)


main()
