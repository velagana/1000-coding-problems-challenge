str = input("Enter the string")
s = str.split()
longest_word = ""
if s == str[::-1]:
    if longest_word >s:
      print(s)