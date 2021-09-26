# initializing string using double quotes or single quote
# if a string is multiplied by a number 'n' then that string is repeated n times

### Challenge 4: string transformation
# Given a getStr() function, write the necessary sequence of operations to transform the string (containing three literals) in such a way that every literal is tripled​ respectively.

# def getStr(s):
#   s=s[:1] + s[0] + s[1:]# Transform the string 
#   s=s[:1] + s[0] + s[1:]
#   s=s[:3] + s[3] + s[3:]
#   s=s[:3] + s[3] + s[3:]
#   s=s[:6] + s[6] + s[6:]
#   s=s[:6] + s[6] + s[6:]
#   # Update the length of string
#   strlen = len(s)
#   return [s, strlen]

# print(getStr('abc'))

### Challenge 5: Find index of a specific value in a string
# Given a string, use a findOccurence(s) function that allows you to find the first occurrences of "b" and "ccc"​ in the string.

# def findOccurence(s):
#   a = s.find("b")
#   b = s.find("ccc") # .find will return the index of the input character

#   return [a,b]

# print(findOccurence('aaabbbccc'))

### challenge 6: lowercase to uppercase

def changeCase(s):
  a = s.upper()
  b = s.lower()

  return [a,b]

print(changeCase('abcdwefa'))