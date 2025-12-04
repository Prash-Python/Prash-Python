def generateElectricityBill(units_consumed):
    print("Calculating electricity bill...")
    if units_consumed <= 100:
        bill_amount = units_consumed * 5
    elif units_consumed <= 200:
        bill_amount = (100 * 5) + ((units_consumed - 100) * 7)
    else:
        bill_amount = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)
    bill_amount += fixed_charge
    print(f"Total electricity bill for {units_consumed} units is: {bill_amount} currency units")
fixed_charge = 100.0
generateElectricityBill(float(input("Enter units consumed: ")))