# Check The Palindrome
def palindrome(word):
    return word == word[::-1]

# Input
word = input ("Input String = ")

# Check The Input
if palindrome(word):
    print(word,"is palindrome")
else:
    print(word,"not palindrome")
