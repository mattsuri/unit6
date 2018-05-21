#Matthew Suriawinata
#5/21/18
#quiz6.py


dictionary = open("engmix.txt")

def program1():
    letter = input("Enter a letter: ")
    for words in dictionary:
        letterCount = words.count(letter)
        if letterCount == 4:
            print(words.strip())
program1()

