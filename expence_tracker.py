# Expence Tracker 

expencesList=[]  # list of expences in form of dictionary
print("===Welcome To Expence Tracker: Save Money Bro")
while True:
    print("-- MENU --")
    print("1. Add Expence")
    print("2. View All Expence")
    print("3. View Total Spent")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice :"))
     # Add Expence
    if (choice==1):
        date=input("Enter The Date")
        category=input("Type of Category")
        description=input("Enter Your Details:")
        amount=float(input("Enter Amount"))

        expence={
            "Date": date,
            "Category": category,
            "amount": amount,
        }
        expencesList.append(expence)
        print("\nCOOL,Exppences is Added successfully")

        # View Expence
    elif(choice == 2):
        if(len(expencesList) == 0):
            print("No Expence Added")
        else:
            print("=== This is Expences")
            count = 1
            for eachexpense in expencesList:
                print(f" Expenxe Number {count} --> {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']} ")
                count += 1
        # View Total Spent
    elif(choice==3):
            
            total=0
            for eachexpense in expencesList:
                total=total+eachexpense["amount"]

                print("\n Total Spent:", total)

#  Exit
    elif(choice==4):
         print("Thank You For Using Expence Tracker")
         break
    else:
         print("Invalid Choice, Please try Again")