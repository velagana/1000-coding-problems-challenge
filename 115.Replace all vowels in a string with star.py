text = input("Enter the string: ")
vowels = "AEIOUaeiou"

result = ""

for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char

print(result)
