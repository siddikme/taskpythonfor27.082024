def remove_first_letter():
    s = input("Enter a string: ")
    result = s[1:] if len(s) > 0 else s
    print("Result after removing the first letter:", result)


remove_first_letter()
