print("Smallest Factor on n \nCreated by: Clyde Joshua C. Belongilot")
print("--------------------------------------------------------------")

while True:
    n1 = int(input("Enter an integer: "))

    if n1 < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        break
    
    elif n1 >= 2:
        for n2 in range(2, n1):
            if n1 % n2 == 0:
                print("Smallest factor other than 1 for", n1,"is", n2)
