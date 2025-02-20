vowls = ["a","e","i","o","u"]
word = input("Input: ")
for i in word:
    if i.lower() in vowls:
        word = word.replace(i,'')
print("Output:",word)
