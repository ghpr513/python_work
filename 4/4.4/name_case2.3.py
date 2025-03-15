#2.3
name = "Eric"
message = f"Hello {name},would you like to learn Python today?"
print(message)

#2.4
first_name = "Eric"
last_name = "Tom"
full_name = f"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

#2.5 2.6
famous_name = "Albert Einstin"
message = f'{famous_name} once said,"A person who never made a mistake never tried anything new."'
print(message)

#2.7
name = '\tAlbert Einstin\n'
print(name)
print(name.lstrip())
print(name.rsplit())
print(name.strip())

#2.8
filename = 'python_note.txt'
print(filename.removesuffix('.txt'))
