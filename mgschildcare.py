def main():
    choice = 0
    name_list = []
    while choice != 5:
        print("1. Drop off a child")
        print("2. Pick up a child")
        print("3. Calculate cost")
        print("4. Print roll")
        print("5. Exit the system")
        print()
        choice = int(input("Choose number between 1 and 5: "))
        print()

        if choice == 1:
            dropOff(name_list)

        elif choice == 2:
            pickUp(name_list)

        elif choice == 3:
            number = len(name_list)
            print(f"The total cost for looking after {len(name_list)} children is \n"
                  f" {calcCost(number):.2f}")

        elif choice == 4:
            prtRoll(name_list)

        else:
            exit("Thank you for using our program!")


def dropOff(name_list):
    name = input("What is the child's name? ")
    name_list.append(name)
    print()
    print(f"Your child {name} is checked in!")


def pickUp(name_list):
    while True:
        try:
            name = input("What is the child's name? ")
            name_list.remove(name)
            print()
            print(f"Your child {name} is checked out!")
            print()
            break

        except ValueError:
            print()
            print("Please type child's name again.")
            print()


def calcCost(number):
    rate = 12.00
    time = int(input("How many hours? "))
    cost = number * rate * time
    return cost


def prtRoll(name_list):
    print()
    print(f"Here are current lists of children in childcare:\n"
          f"{name_list}")
    print()


print("-------------------------------------------------")
print("Welcome to MGS Childcare \n"
      "What would you like to do? Please choose one of the job below")
print("-------------------------------------------------")
print()
main()
