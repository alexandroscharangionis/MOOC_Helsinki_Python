def palindromes(word):
    reversed = ''
    for i in range(len(word) - 1, -1, -1):
        reversed += word[i]
    if reversed == word:
        return True
    else:
        return False


while True:
    palindrome = input("Please type in a palindrome: ")
    if palindromes(palindrome):
        print(f"{palindrome} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
