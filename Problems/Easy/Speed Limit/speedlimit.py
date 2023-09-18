nb = input()
output=""

while nb != "-1":
    distance = 0
    currentTime = 0
    for i in range(int(nb)):
        userInput = input()
        speed = int(userInput.split()[0])
        time = int(userInput.split()[1])
        if i > 0:
            tempTime = time
            time = time - currentTime
            currentTime = tempTime
        else:
            currentTime = time
        distance += speed * time
    output += f"{distance} miles\n"
    nb = input()
print(output)