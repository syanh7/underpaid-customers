def underpaid(name, melons, paid):
    melon_cost = 1.00
    expected = melons * melon_cost
    if expected != paid:
        print(f"{name} paid ${paid:.2f},",
            f"expected ${expected:.2f}"
            )

def main():
    customer_list = [["Joe", 5, 5.00], ["Frank", 6, 6.00], ["Sally", 3, 3.00], ["Sean", 9, 9.50], ["David", 4, 4.00], ["Ashley", 3, 2.00]]
    
    for ele in customer_list:
        name, melons, paid = ele
        underpaid(name, melons, paid)

    file = open("customer-orders.txt")
    
    for line in file:
        line = line.rstrip()
        customer = line.split("|")
        number, name, melons, paid = customer
        underpaid(name, float(melons), float(paid))


    

main()