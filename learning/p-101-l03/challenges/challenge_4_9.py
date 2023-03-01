#translate
# Write a program called translate.py that asks the user for some input
# with the following prompt: Enter some text:
# Use .replace() to convert the text entered by the user into leetspeak
# by making the following changes to lowercase letters:
# The letter a becomes 4
# The letter b becomes 8
# The letter e becomes 3
# The letter l becomes 1
# The letter o becomes 0
# The letter s becomes 5
# The letter t becomes 7

text = input("Your input: ")
translated_text = text.replace("a", "4").replace("b", "8").replace("e", "3").replace("l", "1").replace("o", "0").replace("s", "5").replace("t", "7")
print(translated_text)

#another way:
text = input("Your input: ")

text = text.replace("a", "4")
text = text.replace("b", "8")
text = text.replace("e", "3")
text = text.replace("l", "1")
text = text.replace("o", "0")
text = text.replace("s", "5")
text = text.replace("t", "7")

print(text)

