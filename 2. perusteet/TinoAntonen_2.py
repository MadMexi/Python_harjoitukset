#1. Basic Replacement
#    Task: Replace all occurrences of 'python' with 'Python' in the string "i love python programming in python"
#    Hint: Use the `replace()` method
print("1.")
Python = ("i love python programming in python")
a = Python.replace ("python","Python")
print(a)

#2. Letter Case Swap
#    Task: Convert "Hello World" so each lowercase letter becomes uppercase and vice versa
#    Hint: Use the `swapcase()` method
print("2.")
txt = ("Hello World")
vaihto = txt.swapcase()
print(vaihto)

# 3. Substring Extraction
#    Task: Extract the word "World" from "Hello World!" using string slicing
#    Hint: Use index slicing with starting and ending positions
print("3.")
txt1 = ("Hello World!")
print(txt1[0:5])

#4. Remove Whitespace
#    Task: Remove all leading and trailing whitespace from "   Python is awesome!   "
#    Hint: Use `strip()`
print("4.")
txt2 = ("   Python is awesome!   ")
x1 = txt2.strip()
print(x1)

# 5. String Centering
#    Task: Center the text "Python" in a string of length 20, filling with '*' characters
#    Hint: Use the `center()` method
print("5.")
txt3 = ("Python")
x2 = txt3.center(20)
print(x2)

# 6. First Letter Capitalization
#    Task: Capitalize the first letter of each word in "python is a great language"
#    Hint: Use `title()`
print("6.")
txt4 = ("python is a great language")
x3 = txt4.title()
print(x3)

# 7. Character Count
#    Task: Count how many times the letter 'a' appears in "banana sandwich"
#    Hint: Use the `count()` method
print("7.")
txt5 = ("banana sandwich")
x4 = txt5.count("a")
print(x4)

















