import random
import string

a = input("Enter the sentence: ")
code = int(input("For code press 1 and for decode press 0 "))
if (code == 1):
    sentence = a.split()
    nw = []

    for word in sentence:
        if (len(word) >= 3):
            f = ''.join(random.choices(string.ascii_lowercase, k=3))
            b = ''.join(random.choices(string.ascii_lowercase, k=3))
            nword = f + word[1:] + word[0] + b
            nw.append(nword)
        else:
            nword = word[::-1]
            nw.append(nword)

    print(" ".join(nw))

else:
    sentence = a.split(" ")
    nw = []
    for word in sentence:
        if (len(word) >= 3):
            word = word[-4] + word[3:-4]
            nw.append(word)
        else:
            word = word[::-1]
            nw.append(word)
    print(" ".join(nw))

