def atm_projcts():
    balance=1000    #starting balane
    is_running=True
    print("---THIS IS AN SMALL ATM---")

    while is_running:
        print("\n1. Blanace\n2. Deposit \n3. Withdraw\n4. Exit")
        choice=input("choose according to your case:")

        match choice:  #The match statement replaces"if/else
            case "1":
                print("Balance:${balance}")

            case "2":
                amount=float(input("Deposit amount:"))
                balance+= amount
                print("Done!")


            case "3":
                amount=float(input("Withdraw Amount:"))
                if amount<=balance:
                    balance-=amount
                    print("Done!")

            case "4":
                print("Thanks! & Bye!")
                is_running=False

            case _:
                print("Inavlid choice, try again.")

atm_projcts()           