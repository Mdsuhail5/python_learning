# find the most repeated character
string = "Hello, how are you?"
dict1 = {}
for char in string:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1
print(dict1)
dict1_sorted = sorted(dict1.items(), key=lambda kv: kv[1], reverse=True)
print(dict1_sorted[0])
