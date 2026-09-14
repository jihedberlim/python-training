print("Sale!")

purchase_total = float(input("Please, enter the total purchase amount for the customer: "))
payment_method = int(input("Select the payment method: 1 - bank slip or 2 - credit card: "))

if payment_method == 1:
    purchase_discount = purchase_total * 0.05
    print(
        f"The purchase total of R$ {purchase_total:.2f} was discounted due to payment via bank slip. The customer must pay R$ {purchase_discount:.2f}.")
else:
    installments = int(input("Please specify the desired number of installments: "))
    installment_amount = purchase_total / installments
    print(
        f"The total purchase amount of R$ {purchase_total:.2f} will be paid in {installments} installments of R$ {installment_amount:.2f}.")