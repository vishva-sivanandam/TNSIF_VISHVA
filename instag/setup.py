print("---------- WELCOME TO INSTAG! ----------")
path = input("paste your path here:")

with open('data.txt','w') as file:
    file.write("")
    file.write(path)

print("---------- INSTAG IS READY TO USE! ----------")