# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)
print("Welcome to the blind auction.")
bid_dict = {}
again = True
while again:
    name = input("What is your name?: \n")
    price = input("What's your bid?: $\n")
    bid_dict[name] = price
    bid_again = input("Are there any other  bidders Nigger? Type 'yes' or 'no'\n").lower()
    if bid_again == "no":
        again = False
        keymax = max(bid_dict, key=bid_dict.get)
        print(f"The winner is {keymax} with a bid of ${bid_dict[keymax]}")
    else:
        print("\n" * 100)


#you can call this function instead of having that key_max variable operation
#That we have defined using some cryptic function called max()
def find_highest_bidder(get_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")