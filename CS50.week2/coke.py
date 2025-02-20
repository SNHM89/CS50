amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    payment = int(input("insert coin: "))
    if payment in [5,10,25] :
        amount_due -= payment
    else: 
        continue

print(f"Change Owed: {abs(amount_due)}")