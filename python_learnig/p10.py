#Program to check if the alphabet is Vowel or Consonant

vowels = ['a','e','i','o','u']
input_char = input("Enter an alphabet: ")
if input_char in vowels:
    print(f"{input_char} is a Vowel")
else:
    print(f"{input_char} is a Consonant")