print("Welcome to the restaurant simulator.")

kilo_price = float(input("Please state the price charged per kilogram: "))
plate_weight = float(input("Enter the weight of the customer's plate (in kg): "))

plate_price = kilo_price * plate_weight

print(f"The price of the dish is R$ {plate_price:.2f}")

if plate_weight > 1:
    print("If the customer's plate exceeds 1 kg, apply a fixed price of R$ 80.00.")