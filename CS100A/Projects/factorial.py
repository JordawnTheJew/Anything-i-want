while True:


    fact = int(input('enter a number to get its factor: '))

    if fact <= 0:
        print ("sorry that number cannot be factored")
    elif fact == 0:
        print ("0's factorial is 1")
    else:
        for i in range(1,fact + 1):
            factorial = fact*i
        print("The factorial of",fact,"is",factorial)


    play_again = input("Enter in another number to factor? (y/n): ")
    if play_again.lower() != "y":
        break    