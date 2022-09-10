#1 Palindrome implimantation
number=input("Enter any number :")
i=0
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break

# 2 - Sum of 2 digits into output
def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10

    return sum


n = int(input("Enter the no :"))
print(getSum(n))

# 3 - Reverse a string only alphabets.
def reverseString(text):
    index = -1

    # Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text

string = "ab@#cd!ef"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))

# 4 - Duplicate count in Dictonary format
from collections import Counter

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]

counts = dict(Counter(some_list))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)

# 5 -

# 6 - Python program to remove leading zeros from an IP address.
str1 = "216.08.094.196"
res=str1.replace("0", '')
print(res)

# 7 -
items = [1,2,[3,4,[5,6]],7,8,[9,[10]]]
new_list = []
[new_list.extend(x) if type(x) is list else new_list.append(x) for x in items]
print(new_list)