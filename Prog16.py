text = "Python Programming."
# i. Display Python
print(text[:6])
# ii. Display Programming
print(text[7:18])
# iii. Check whether Java is present
if "Java" in text:
    print("Java is present")
else:
    text = "Python Java Programming."
    print("Java was not present, so it was added.")
# iv. Find the length of the new string
print("Length of string:", len(text))
# v. Count the number of words
print("Number of words:", len(text.split()))
# vi. Capitalize each word
print("Capitalized:", text.title())
# vii. Remove all spaces
print("Without spaces:", text.replace(" ", ""))
# viii. Frequency of A, P, R, M in capital letters
print("Frequency of A:", text.upper().count("A"))
print("Frequency of P:", text.upper().count("P"))
print("Frequency of R:", text.upper().count("R"))
print("Frequency of M:", text.upper().count("M"))