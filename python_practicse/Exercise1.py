# find the most repeated character in this text
from pprint import pprint
sentence = "This is a common interview question"
frequence = {}
for char in sentence:
    if char in frequence:
        frequence[char] += 1
    else:
        frequence[char] = 1
pprint(frequence)
frequence_sorted = sorted(
    frequence.items(), key=lambda kv: kv[1], reverse=True)
pprint(frequence_sorted[0])
