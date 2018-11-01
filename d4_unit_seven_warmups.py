my_name = "Brian"
new_name = ""

for letter in my_name:
    if letter == "i":
        new_name = new_name + "y"
    else:
        new_name = new_name + letter

print(new_name)