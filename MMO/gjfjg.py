
import string

str1 = str(input("Enter word: "))
def func(simb):
    count = 0
    for char in str1:
        if char.isalpha():
            count+= 1
    return count
print("kol-vo words in string: ", func(str1))