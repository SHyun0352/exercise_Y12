def corrector(question_text):

    while True:
        try:

            number = float(input(question_text))

            if number != 0:
                return number

        except ValueError:
            pass

        print("You have typed an incorrect amount.")


def yes_no(question_text):

    while True:

        answer = input(question_text).lower()

        if answer in ["yes", "y"]:
            return "Yes"

        elif answer in ["no", "n"]:
            return "No"

        print("Invalid answer. Please type 'yes' or 'no'.")


def item_sell():
    highest_bid = 0

    while True:

        item = input("What is this auction for? ")
        confirmation = yes_no(f"Are you sure you want to sell {item}? (Y/N) ")
        reservep = corrector("What is the reserve price? ")

        if confirmation == "Yes":
            bid(item, reservep, highest_bid)

            redo = ""

            print()
            redo = yes_no("Do you want to sell another item? (Y/N)" )

            if redo != "Yes":
                print()
                exit("Thank you for using our auction!")

        elif confirmation == "X" or "x":
            print()
            exit("Thank you for using our program!")

        else:
            print()


def bid(_item, _reservep, _highest_bid):

    bid_price = 0

    print()
    print(f"The auction for the {_item} has started! \n"
          f"Current reserve price: {_reservep}")

    while not bid_price == -1:

        bid_price = corrector("What is your bid? ")

        if bid_price > _highest_bid:
            _highest_bid = bid_price
            print()
            print(f"Highest bid so far is ${_highest_bid}")

        elif bid_price == -1:
            print()
            print(f"The auction for the {_item} finished with a bid of {_highest_bid}")

        else:
            _highest_bid = _highest_bid
            print()
            print(f"please enter a higher bid \n"
                  f"Current highest bid is ${_highest_bid}.")


# Main routine
print("Welcome to silent Auction!")
print()
item_sell()
