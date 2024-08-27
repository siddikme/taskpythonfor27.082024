def reverse_and_upper(text):
    reversed_text = text[::-1] 
    upper_text = reversed_text.upper()  
    return upper_text

text = input("Enter a text: ")

result = reverse_and_upper(text)
print("Reversed and uppercased text:", result)
