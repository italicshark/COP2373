# Alex Akulov
# 8/27/26
# This program sell a limited number of cinema tickets
# Counts all the buyers and every buyer can buy up to 4

# function asking the user how many they would like to buy
def get_ticket():
    tickets = int(input("Enter how many tickets you need?: "))
    return tickets

# function displaying how many tickets after user purchase
def display_result(total_tickets):
    print("Tickets remaining: ", total_tickets)

# beginning variable
def main():
    total_tickets = 10
    buyers = 0

# loop until tickets end
    while total_tickets > 0:
        display_result(total_tickets)
        tickets_requested = get_ticket()

    # user may only buy between 1 and 4 tickets
        if tickets_requested < 1 or tickets_requested > 4:
            print("You may purchase between 1 and 4 tickets!")

    # only 20 tickets no more
        elif tickets_requested > total_tickets:
            print("There are not enough tickets!")

    # buyer and ticket counter
        else:
            total_tickets = total_tickets - tickets_requested
            buyers += 1

            display_result(total_tickets)

    # print results
    print("All tickets have been sold!")
    print("Total number of buyers:", buyers)
main()
