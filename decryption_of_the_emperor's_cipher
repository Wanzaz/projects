
letters = "abcdefghijklmnopqrstuvwxyz"
status = True
word = input("Enter the word:  ")
key = int(input("Enter key (1-26):  "))
    
result = ""
if key < 1:
    key = 2
elif key > 26:
    key = 25

for i in word:
    try:
        position = letters.find(i)
        result = result + letters[position - key]
    except:
        position = letters.find(i)
        position = 26 - position
        position = key + position
        result = result + letters[position]
print(result)
     
