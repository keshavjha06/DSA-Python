def profit_or_loss(cp, sp):
    if sp > cp:
        print("Profit is", sp - cp)
    elif cp > sp:
        print("Loss is", cp - sp)
    else:
        print("No Profit No Loss")


cp = int(input("Enter CP: "))  # cost price
sp = int(input("Enter SP: "))  # selling price
profit_or_loss(cp, sp)
