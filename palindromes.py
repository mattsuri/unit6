#Matthew Suriaiwnata
#5/17/18
#warmup17.py

dictionary = open("engmix.txt")

for word in dictionary:
    word = word.strip()
    reg = list(word)
    reg.reverse()
    if list(word) == reg:
        print(word)
    
    
    

