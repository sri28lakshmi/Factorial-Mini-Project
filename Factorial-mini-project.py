def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n - 1)

def main():
    while True:
        print("Welcome to FACTORIAL!\nPress 1: Start\nPress 2: Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num = int(input("Enter Number: "))
            print(f"The value of {num}! is:", factorial_recur(num))
        elif choice == 2:
            exit()
        else:
            print("Please enter a valid choice!")

main()
