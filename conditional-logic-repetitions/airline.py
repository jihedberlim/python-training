client_type = input("Please, specify the customer type: Premium, Gold, or Regular: ")
luggage_weight = float(input("Provide the weight of the baggage the customer wishes to check: "))

if client_type.capitalize() == "Premium":
    if luggage_weight <= 32:
        print(f"Customer {client_type} cleared to take luggage")
    else:
        excess_weight = luggage_weight - 32
        print(f"{client_type} customers are entitled to check in baggage weighing up to 32 kg. \nThe current baggage exceeds this weight limit by {excess_weight:.2f} kg. \nPlease proceed to the payment counter to pay the fee for the excess weight.")
elif client_type.capitalize() == "Gold":
    if luggage_weight <= 28:
        print(f"Customer {client_type} cleared to take luggage")
    else:
        excess_weight = luggage_weight - 28
        print(f"{client_type} customers are entitled to check in baggage weighing up to 28 kg. \nThe current baggage exceeds this weight limit by {excess_weight:.2f} kg. \nPlease proceed to the payment counter to pay the fee for the excess weight.")
else:
    print(f"{client_type} customers are not entitled to free baggage. \nPlease proceed to the payment counter to pay for your baggage.")