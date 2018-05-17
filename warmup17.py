#Matthew Suriaiwnata
#5/17/18
#warmup17.py



file = open('engmix.txt')

for line in file:
    words = line.strip()
    if "m" in words and "a" in words and "t" in words and "h" in words and "e" in words and "w" in words:
        print(words)