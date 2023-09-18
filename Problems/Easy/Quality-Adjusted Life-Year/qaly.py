iterationNb = int(input())
qaly = 0
for x in range(iterationNb):
    userInput = input()
    nbYear = userInput.split()[0]
    nbQuality = userInput.split()[1]
    qaly += float(nbYear) * float(nbQuality)
print("{:10.3f}".format(qaly))