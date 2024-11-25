def part1():

    counter = 0
    with open("p1.txt", "r") as file:
        for i, char in enumerate(file.read()):
            if counter < 0:
                print(f"he has entered basement at {i}")
                break
            if char == '(':
                counter += 1
            else:
                counter -= 1

    print(counter)


part1()
