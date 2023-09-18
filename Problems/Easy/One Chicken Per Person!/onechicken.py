userInput = input()
nbPeople = int(userInput.split()[0])
nbChicken = int(userInput.split()[1])
nb = nbChicken - nbPeople
nb = int(nb)

if nb >= 0:
    if nb == 1:
        print(f"Dr. Chaz will have {nb} piece of chicken left over!")
    else:
        print(f"Dr. Chaz will have {nb} pieces of chicken left over!")
else:
    nb = abs(nb)
    if nb == 1:
        print(f"Dr. Chaz needs {abs(nb)} more piece of chicken!")
    else:
        print(f"Dr. Chaz needs {abs(nb)} more pieces of chicken!")