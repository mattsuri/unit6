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





def program3():
    letter = input("Enter a letter: ")
    num = int(input("Enter a number: "))
    for words in dictionary:
        letterCount = words.count(letter)
        length = len(words)
        if letterCount == 4 and length == num:
            print(words.strip())
program3()


def program4():
    list10 = []
    for words in dictionary:
        length = len(words)
        if length >= 10:
            list10.append(words)
    print(list10[8000])
program4()


def program5():
    vowelCount = 0 
    lastCount = 0
    vowelWord = ""
    for words in dictionary:
        vowelCount += words.count("a")
        vowelCount += words.count("e")
        vowelCount += words.count("i")
        vowelCount += words.count("o")
        vowelCount += words.count("u")
        if vowelCount > lastCount:
            vowelCount = lastCount
            vowelWord = words
    print(vowelWord)
program5()