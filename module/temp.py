acronym = input("What acronym do you want to add?\n")
definition = input("What is the definition?\n")

# Open the file in append mode ('a') to add new entries without overwriting
with open('acronyms.txt', 'a') as file:
    file.write(acronym + " - " + definition + '\n')

print(f"The acronym '{acronym}' with definition '{definition}' has been added.")
