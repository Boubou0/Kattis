input()
numbers = input().split()
expense = 0
for nb in numbers:
    if nb.startswith("-"):
        nb = nb.replace(nb[0], "", 1)
        expense += int(nb)

print(expense)