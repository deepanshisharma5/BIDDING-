#project
#bidding project 


print('''
                         ___________
                         \         / 
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                        
                       .-------------.
                      /_______________\ 

''')

print("Welcome to the Auction of the mansion. \nLet's start bidding!")

# Dictionary to store all bids
bids = {}
bidding_finished = False

# Function to determine the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\n🏆 The winner is **{winner}** with a bid of **${highest_bid}**! 🥇")

# Start bidding loop
while not bidding_finished:
    name = input("\nWhat is your name?: ")
    
    # Input validation for bid amount
    try:
        bid_amount = int(input("What is your bid?: $"))
    except ValueError:
        print("❌ Please enter a valid number for the bid.")
        continue

    bids[name] = bid_amount

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue != 'yes':
        print("⚠️ Invalid input. Assuming no more bidders.")
        bidding_finished = True
        find_highest_bidder(bids)
